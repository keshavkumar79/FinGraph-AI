from fastapi import APIRouter, HTTPException

from app.api.transactions import graph_service
from app.services.transaction_service import TransactionService


router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.get("/{account_id}")
def get_account(account_id: str):

    transaction_service = TransactionService(
        graph_service.graph
    )

    statistics = transaction_service.get_account_statistics(
        account_id
    )

    if statistics is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return statistics