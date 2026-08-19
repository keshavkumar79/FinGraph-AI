import networkx as nx


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