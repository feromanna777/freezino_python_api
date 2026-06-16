# app/routers/contact.py
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/contact", tags=["contact"])

@router.post("")
def submit_contact():
    raise HTTPException(status_code=501, detail="Not implemented yet")