from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.security import get_password_hash

class UserService:
    @staticmethod
    async def create_user(db: Session, user: UserCreate) -> User:
        db_user = User(
            full_name=user.full_name,
            email=user.email,
            password=get_password_hash(user.password),
            role=user.role,
            recovery_email=user.recovery_email,
            phone_number=user.phone_number
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    async def get_user_by_email(db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    async def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
        db_user = db.query(User).filter(User.id == user_id).first()
        if not db_user:
            return None
            
        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
            
        db.commit()
        db.refresh(db_user)
        return db_user