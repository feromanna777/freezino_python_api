# app/routers/auth.py

from datetime import datetime
from fastapi import APIRouter, HTTPException, status , Depends
import sqlite3
from app.logging import logger
from jose import JWTError
from app.db import get_connection


from app.security import (
    create_access_token,
    get_password_hash,
    verify_password,
    get_current_user,
)
from app.models.user import UserRegister, UserLogin
#
router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/login")
def login_user(user_data: UserLogin):
    conn = None
    try:
        conn =  get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (user_data.email,))
        user_db = cursor.fetchone()

        if user_db is None:
            logger.info("Login attempt with unknown email: %s", user_data.email)
            raise HTTPException(status_code=401, detail="Неверный логин или пароль")

        password_hash_from_db = user_db["password_hash"]

        if not verify_password(user_data.password, password_hash_from_db):
            logger.info("Login attempt with unknown email: %s", user_data.email)
            raise HTTPException(status_code=401, detail="Неверный логин или пароль")



        return {
            "success": True,
            "data": {
                "user": {
                    "id": user_db["id"],
                    "username": user_db["username"],
                    "email": user_db["email"],
                    "balance": user_db["balance"],
                },
                "access_token": create_access_token(data={"sub": user_data.email}),
                "refresh_token": "fake2",
            },
        }

    except JWTError as e:
    # Ошибка генерации токена: логируем, клиенту — 500 (это баг на нашей стороне)
        logger.exception("JWT creation failed for email: %s", user_data.email)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка аутентификации"
        )


    finally:
        if conn:
            conn.close()

@router.post("/register")
def register_user(user: UserRegister):
    hashed_password = get_password_hash(user.password)
    conn = None
    try:
        conn = get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO users (username, email, password_hash, balance)
            VALUES (?, ?, ?, ?)
            """,
            (user.username, user.email, hashed_password, 1000.0),
        )
        conn.commit()
        new_user_id = cursor.lastrowid
        logger.info("User registered successfully: %s", user.email)

        return {
            "success": True,
            "data": {
                "user": {
                    "id": new_user_id,
                    "username": user.username,
                    "email": user.email,
                    "balance": 1000.0,
                },
                "access_token": create_access_token(data={"sub": user.email}),
                "refresh_token": "fake2",
            },
        }
    except sqlite3.IntegrityError as e:
        # Ожидаемая бизнес-ошибка: дубликат email/username
        logger.warning(
            "Registration failed (duplicate): email=%s, username=%s, error=%s",
            user.email, user.username, str(e)
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким username или email уже существует",
        )
    finally:
        if conn:
            conn.close()

@router.get("/me")
def read_users_me(current_user=Depends(get_current_user)):
    return {
        "user": {
            "id": current_user["id"],
            "username": current_user["username"],
            "email": current_user["email"],
            "balance": current_user["balance"],
            "avatar": current_user["avatar"],
        }
    }
