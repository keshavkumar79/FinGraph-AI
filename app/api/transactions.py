from fastapi import APIRouter
from typing import List

from app.models.transaction import Transaction
from app.services.graph_service import GraphService


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


graph_service = GraphService()


@router.post("/")
def add_transactions(transactions: List[Transaction]):

    graph_service.add_transactions(transactions)

    return {
        "message": "Transactions added successfully",
        "transactions_added": len(transactions),
        "accounts": graph_service.get_account_count(),
        "connections": graph_service.get_transaction_count()
    }