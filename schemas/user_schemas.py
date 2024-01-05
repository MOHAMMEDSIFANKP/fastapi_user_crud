from pydantic import BaseModel, EmailStr
from typing_extensions import Optional

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None

class UsersBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: bool

class UserData(UsersBase):
    id: int

class UserCreate(UsersBase):
    password : str

class UserSignin(BaseModel):
    email: EmailStr
    password : str
