from pydantic import BaseModel


class AccountRisk(BaseModel):
    account_id: str
    incoming_transactions: int
    outgoing_transactions: int
    incoming_amount: float
    outgoing_amount: float