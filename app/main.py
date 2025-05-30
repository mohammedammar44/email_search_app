from fastapi import FastAPI
from .routes import router
from app.routes import router 
from .database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Creates the emails table if not exists

app.include_router(router)
