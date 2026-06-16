# app/routers/stats.py
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/api/stats", tags=["stats"])

@router.get("/casino")  # Путь из задачи: /api/casino/stats
def casino_stats():
    return {"success": True, "data": {"total_bets": 0, "total_won": 0}, "message": "Not implemented yet"}

@router.get("/countries")
def countries_stats():
    return {"success": True, "data": [], "message": "Not implemented yet"}

@router.get("/countries/{code}")
def country_stats(code: str):
    # По заданию здесь должен быть 404
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")