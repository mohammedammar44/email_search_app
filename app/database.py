from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session


DATABASE_URL = "mysql+pymysql://root:YourPass@localhost:3306/email_app"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ✅ Add this function so FastAPI can get DB sessions via dependency injection
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
