from fastapi import HTTPException, status
from passlib.context import CryptContext
from datetime import datetime
from jose import jwt
from models import user_model
from schemas import user_schemas
from backend.settings import SECRET_KEY, ALGORITHM, access_token_expires, refresh_token_expires

password_hash = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_user_by_email(email: str, db):
    existing_user = db.query(user_model.User).filter(user_model.User.email == email).first()
    if not existing_user:
        return None
    return existing_user

def get_user_by_id(id: int, db):
    existing_user = db.query(user_model.User).filter(user_model.User.id == id).first()
    if not existing_user:
        return None
    return existing_user

def get_all_users(db):
    return db.query(user_model.User).all()

def authenticate(email: str, password: str, db):
    user  = get_user_by_email(email, db)
    if not user or not verify_password(password, user.password):
        return None
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not activated. Please contact support.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def create_tokens(data: dict):
    to_encode = data.copy()

    # Access token
    access_expire = datetime.utcnow() + access_token_expires
    to_encode.update({"exp": access_expire})
    access_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    # Refresh token
    refresh_expire = datetime.utcnow() + refresh_token_expires
    to_encode.update({"exp": refresh_expire})
    refresh_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return access_token, refresh_token


def create_user(user_data: user_schemas.UserCreate, db):
    user_instance = user_model.User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        is_active = user_data.is_active,
        password=password_hash.hash(user_data.password),
    )
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)
    return user_instance