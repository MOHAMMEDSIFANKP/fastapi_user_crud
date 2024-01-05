from fastapi import FastAPI
from backend.database import engine
from routers.auth_router import router as auth_router
from models import user_model
app = FastAPI()


user_model.Base.metadata.create_all(bind=engine)
app.include_router(auth_router, prefix='/auth', tags=['authendication'])

