# app/routers/shop.py
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/shop", tags=["shop"])

@router.get("/items")
def list_items():
    return {"success": True, "data": [], "message": "Not implemented yet"}

@router.get("/my-items")
def list_my_items():
    return {"success": True, "data": [], "message": "Not implemented yet"}

@router.post("/buy/{item_id}")
def buy_item(item_id: int):
    raise HTTPException(status_code=501, detail="Not implemented yet")

@router.post("/sell/{user_item_id}")
def sell_item(user_item_id: int):
    raise HTTPException(status_code=501, detail="Not implemented yet")

@router.post("/equip/{item_id}")
def equip_item(item_id: int):
    raise HTTPException(status_code=501, detail="Not implemented yet")