from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.users import UserService
from app.schemas.user import UserCreate, UserUpdate, UserInDB

class UserController:
    @staticmethod
    async def create_user(db: Session, user: UserCreate) -> UserInDB:
        db_user = await UserService.get_user_by_email(db, user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return await UserService.create_user(db, user)

    @staticmethod
    async def update_user(db: Session, user_id: int, user_update: UserUpdate) -> UserInDB:
        updated_user = await UserService.update_user(db, user_id, user_update)
        if not updated_user:
            raise HTTPException(status_code=404, detail="User not found")
        return updated_user