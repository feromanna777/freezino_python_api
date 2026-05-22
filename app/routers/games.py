# app/routers/games.py
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/games", tags=["games"])
@router.get("/roulette/recent")
def recent_roulette():
    return {"success": True, "data": [], "message": "Not implemented yet"}

@router.post("/roulette/bet")
def roulette_bet():
    raise HTTPException(status_code=501, detail="Not implemented yet")

@router.post("/slots/spin")
def slots_spin():
    raise HTTPException(status_code=501, detail="Not implemented yet")

@router.post("/crash/bet")
def crash_bet():
    raise HTTPException(status_code=501, detail="Not implemented yet")

@router.post("/hilo/bet")
def hilo_bet():
    raise HTTPException(status_code=501, detail="Not implemented yet")

@router.post("/wheel/spin")
def wheel_spin():
    raise HTTPException(status_code=501, detail="Not implemented yet")

@router.get("/sessions")
def get_sessions():
    return {"success": True, "data": [], "message": "Not implemented yet"}
