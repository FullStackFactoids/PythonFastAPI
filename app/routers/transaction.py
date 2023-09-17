from fastapi import APIRouter
from app.models.transaction import Transaction

router = APIRouter()

transactions = []


@router.post("/")
def create_transaction(transaction: Transaction):
    transactions.append(transaction)
    return transaction


@router.get("/")
def read_transactions():
    return transactions


@router.get("/{transaction_id}")
def read_transaction(transaction_id: int):
    return transactions[transaction_id]


@router.put("/{transaction_id}")
def update_transaction(transaction_id: int, transaction: Transaction):
    transactions[transaction_id] = transaction
    return transaction


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int):
    transactions.pop(transaction_id)
    return {"message": "Transaction deleted"}
