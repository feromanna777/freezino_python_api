# app/routers/dev.py
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/dev", tags=["dev"])

@router.post("/seed")
def seed_db():
    raise HTTPException(status_code=501, detail="Not implemented yet")

@router.post("/add-money")
def add_money():
    raise HTTPException(status_code=501, detail="Not implemented yet")

@router.post("/reset-balance")
def reset_balance():
    raise HTTPException(status_code=501, detail="Not implemented yet")