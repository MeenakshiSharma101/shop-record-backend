from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_db_connection
from pydantic import BaseModel
from datetime import date, time

app = FastAPI()

# --------- CORS CONFIG ---------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later you can restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- SCHEMA ----------
class Transaction(BaseModel):
    type: str
    amount: float
    description: str
    date: date
    time: time

# ---------- ROOT ----------
@app.get("/")
def root():
    return {"status": "API is running"}

# ---------- GET ----------
@app.get("/transactions")
def get_transactions():
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="DB connection failed")

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM transactions")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    return data

# ---------- POST ----------
@app.post("/transactions")
def add_transaction(transaction: Transaction):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="DB connection failed")

    cursor = conn.cursor()
    query = """
        INSERT INTO transactions (type, amount, description, date, time)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        transaction.type,
        transaction.amount,
        transaction.description,
        transaction.date,
        transaction.time
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Transaction added successfully"}
