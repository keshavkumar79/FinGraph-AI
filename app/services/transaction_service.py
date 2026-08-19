class TransactionService:

    def __init__(self, graph):
        self.graph = graph

    def get_account_statistics(self, account_id):

        if account_id not in self.graph:
            return None

        incoming_transactions = 0
        outgoing_transactions = 0

        incoming_amount = 0.0
        outgoing_amount = 0.0

        for _, _, _, data in self.graph.in_edges(
            account_id,
            keys=True,
            data=True
        ):
            incoming_transactions += 1
            incoming_amount += data.get("amount", 0)

        for _, _, _, data in self.graph.out_edges(
            account_id,
            keys=True,
            data=True
        ):
            outgoing_transactions += 1
            outgoing_amount += data.get("amount", 0)

        return {
            "account_id": account_id,
            "incoming_transactions": incoming_transactions,
            "outgoing_transactions": outgoing_transactions,
            "incoming_amount": incoming_amount,
            "outgoing_amount": outgoing_amount
        }