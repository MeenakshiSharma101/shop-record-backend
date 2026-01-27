from fastapi import FastAPI, HTTPException
from database import get_db_connection
from pydantic import BaseModel
from datetime import date, time

app = FastAPI(
    title="Shop Record System API",
    description="Backend API for managing shop transactions",
    version="1.0.0"
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
        raise HTTPException(status_code=500, detail="Database connection failed")

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM transactions")
        data = cursor.fetchall()
        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()


# ---------- POST ----------
@app.post("/transactions")
def add_transaction(transaction: Transaction):
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO transactions (type, amount, description, date, time)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            transaction.type,
            transaction.amount,
            transaction.description,
            transaction.date,
            transaction.time
        )

        cursor.execute(query, values)
        conn.commit()
        return {"message": "Transaction added successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        conn.close()
