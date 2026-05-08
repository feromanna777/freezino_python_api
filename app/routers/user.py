# app/routers/user.py
import sqlite3
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from app.db import get_connection
from app.security import get_current_user
from app.logging import logger

router = APIRouter(prefix="/api/user", tags=["user"])
@router.get("/profile")
def get_profile(current_user: Any = Depends(get_current_user)):
    conn=None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE id = ?",
            (current_user["id"],),
        )
        row = cursor.fetchone()
        if row is None:
            logger.warning("User profile not found in DB: id=%s", current_user["id"])
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User profile not found "
            )
        logger.info("Profile accessed: id=%s", current_user["id"])
        return {
            "id": current_user["id"],
            "username": current_user["username"],
            "email": current_user["email"],
            "balance": current_user["balance"],
            "avatar": current_user["avatar"],
            "total_work_time": current_user["total_work_time"],
            "created_at": current_user["created_at"],
        }
    except sqlite3.Error as e:
        logger.exception("Database error in get_profile for user id=%s", current_user["id"])
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error"
        )
    finally:
        if conn is not None:
            conn.close()


@router.get("/balance")
def get_balance(current_user: Any = Depends(get_current_user)):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE id = ?",
            (current_user["id"],),
        )
        row = cursor.fetchone()
        if row is None:
            logger.warning("User balance not found in DB: id=%s", current_user["id"])
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No user found"
            )
        logger.info("Balance checked: id=%s", current_user["id"])
        return {
            "balance": current_user["balance"],
        }
    except sqlite3.Error as e:
        logger.exception("Database error in get_balance for user id=%s", current_user["id"])
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error"
        )
    finally:
        if conn is not None:
            conn.close()


@router.get("/stats")
def get_stats(current_user: Any = Depends(get_current_user)):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE id = ?",
            (current_user["id"],),
        )
        row = cursor.fetchone()
        if row is None:
            logger.warning("User stats not found: id=%s", current_user["id"])
            raise HTTPException(status_code=404, detail="No user found")
        logger.info("Stats fetched: id=%s", current_user["id"])
        return {
            "total_work_time": current_user["total_work_time"],
            "total_earned": current_user["total_earned"],
            "total_lost": current_user["total_lost"],
            "games_played": current_user["games_played"],
        }
    except sqlite3.Error as e:
        logger.exception("Database error in get_stats for user id=%s", current_user["id"])
        raise HTTPException(status_code=500, detail="Database error")



    finally:
        if conn is not None:
            conn.close()