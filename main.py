print("🔥 REAL MAIN.PY DEPLOYED 🔥")

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, time

app = FastAPI()

# ---------------- HEALTH CHECK ----------------
@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# ---------------- TEMP DATA (NO DB) ----------------
fake_transactions = []

class Transaction(BaseModel):
    type: str
    amount: float
    description: str
    date: date
    time: time

@app.get("/transactions")
def get_transactions():
    return fake_transactions

@app.post("/transactions")
def add_transaction(transaction: Transaction):
    fake_transactions.append(transaction)
    return {"message": "Transaction added (no DB)"}
