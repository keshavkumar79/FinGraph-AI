from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Transaction(BaseModel):
    transaction_id: str
    sender: str
    receiver: str
    amount: float
    timestamp: datetime
    transaction_type: str = "UPI"
    device_id: Optional[str] = None
    location: Optional[str] = None