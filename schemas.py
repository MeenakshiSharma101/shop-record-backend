from pydantic import BaseModel
from datetime import date, time


class TransactionCreate(BaseModel):
    type: str
    amount: float
    description: str
    date: date
    time: time
