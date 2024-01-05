from fastapi import APIRouter, Depends, status, HTTPException
from typing_extensions import List
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from services import auth_service
from schemas import user_schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/token', response_model=user_schemas.Token, status_code=status.HTTP_200_OK)
def login(user_data: user_schemas.UserSignin, db: Session = Depends(get_db)):
    user = auth_service.authenticate(user_data.email,user_data.password,db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Please check your email and password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token, refresh_token = auth_service.create_tokens (data={"sub": user.email})
    return {"access_token": access_token,"refresh_token":refresh_token, "token_type": "bearer"}


@router.post("/signup", response_model=user_schemas.UserData, status_code=status.HTTP_201_CREATED,)
def signup(user_data:user_schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = auth_service.get_user_by_email(user_data.email, db)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            detail="Email already registered"
        )
    user = auth_service.create_user(user_data, db)
    return user

@router.get("/user/{id}", response_model=user_schemas.UserData, status_code=status.HTTP_200_OK)
def user_details(id:int, db: Session = Depends(get_db)):
    existing_user = auth_service.get_user_by_id(id, db)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found",
        )
    return existing_user


@router.patch("/user/{id}", response_model=user_schemas.UserData, status_code=status.HTTP_200_OK)
def user_details(id:int,user_data:user_schemas.UsersBase, db: Session = Depends(get_db)):
    existing_user = auth_service.get_user_by_id(id, db)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found",
        )
    for field, value in user_data.dict().items():
        setattr(existing_user, field, value)    
    db.commit()
    db.refresh(existing_user)
    return existing_user  

@router.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT)
def user_details(id:int, db: Session = Depends(get_db)):
    existing_user = auth_service.get_user_by_id(id, db)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found",
        )
    db.delete(existing_user)
    db.commit()
    return {"message": "User deleted successfully"}


@router.get("/users", response_model=List[user_schemas.UserData],status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return auth_service.get_all_users(db)