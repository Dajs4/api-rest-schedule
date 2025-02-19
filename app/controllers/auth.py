from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.auth import AuthService
from app.schemas.user import Token
from app.dependencies import get_db

class AuthController:
    @staticmethod
    async def login(db: Session, email: str, password: str) -> Token:
        user = await AuthService.authenticate_user(db, email, password)
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Incorrect email or password"
            )
        return await AuthService.create_token(user)