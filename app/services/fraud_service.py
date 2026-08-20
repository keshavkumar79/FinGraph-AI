import networkx as nx
from collections import defaultdict
from datetime import timedelta


class FraudService:

    def __init__(self, graph):
        self.graph = graph

    def detect_circular_flows(self):

        cycles = list(nx.simple_cycles(self.graph))

        suspicious_cycles = []

        for cycle in cycles:

            if len(cycle) >= 3:

                suspicious_cycles.append({
                    "pattern": "CIRCULAR_FLOW",
                    "risk": "HIGH",
                    "accounts": cycle,
                    "explanation": (
                        f"A circular transaction flow was detected "
                        f"across {len(cycle)} accounts."
                    )
                })

        return suspicious_cycles

    def detect_velocity(self, window_minutes=10, threshold=3):

        account_transactions = defaultdict(list)

        for sender, receiver, key, data in self.graph.edges(
            keys=True,
            data=True
        ):

            timestamp = data.get("timestamp")

            if timestamp is None:
                continue

            account_transactions[sender].append({
                "timestamp": timestamp,
                "amount": data.get("amount", 0),
                "receiver": receiver
            })

            account_transactions[receiver].append({
                "timestamp": timestamp,
                "amount": data.get("amount", 0),
                "sender": sender
            })

        suspicious_accounts = []

        for account_id, transactions in account_transactions.items():

            transactions.sort(
                key=lambda transaction: transaction["timestamp"]
            )

            for i in range(len(transactions)):

                start_time = transactions[i]["timestamp"]

                count = 0
                total_amount = 0

                for j in range(i, len(transactions)):

                    current_time = transactions[j]["timestamp"]

                    if current_time - start_time <= timedelta(
                        minutes=window_minutes
                    ):
                        count += 1
                        total_amount += transactions[j]["amount"]
                    else:
                        break

                if count >= threshold:

                    suspicious_accounts.append({
                        "account_id": account_id,
                        "pattern": "HIGH_VELOCITY",
                        "risk": "HIGH",
                        "transactions": count,
                        "amount": total_amount,
                        "window_minutes": window_minutes,
                        "explanation": (
                            f"Account {account_id} participated in "
                            f"{count} transactions within "
                            f"{window_minutes} minutes."
                        )
                    })

                    break

        return suspicious_accounts