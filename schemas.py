from pydantic import BaseModel
from datetime import date, time

print("schemas.py loaded")

class TransactionCreate(BaseModel):
    type: str
    amount: float
    description: str
    date: date
    time: time
