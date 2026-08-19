import networkx as nx

from app.models.transaction import Transaction


class GraphService:

    def __init__(self):
        self.graph = nx.MultiDiGraph()

    def add_transaction(self, transaction: Transaction):

        self.graph.add_node(transaction.sender)
        self.graph.add_node(transaction.receiver)

        self.graph.add_edge(
            transaction.sender,
            transaction.receiver,
            transaction_id=transaction.transaction_id,
            amount=transaction.amount,
            timestamp=transaction.timestamp,
            transaction_type=transaction.transaction_type
        )

    def add_transactions(self, transactions):

        for transaction in transactions:
            self.add_transaction(transaction)

    def get_account_count(self):

        return self.graph.number_of_nodes()

    def get_transaction_count(self):

        return self.graph.number_of_edges()