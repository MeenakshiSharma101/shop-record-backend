from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/transactions")
def get_transactions():
    # Temporary dummy data
    return [
        {
            "type": "income",
            "amount": 5000,
            "description": "Sample transaction",
            "date": "2025-01-01",
            "time": "10:00"
        }
    ]
