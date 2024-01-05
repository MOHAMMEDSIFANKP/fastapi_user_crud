from sqlalchemy import Column, Integer, String, Boolean
from backend.database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))
    email = Column(String(length=250), unique=True, index=True, nullable=False)
    password = Column(String(length=250))
    is_active = Column(Boolean, default=False)

