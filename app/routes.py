# app/routes.py or wherever your routes are defined

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.database import get_db  # Adjust import if needed

router = APIRouter()  # ✅ Define router first

@router.get("/search/")
def search_emails(q: str, db: Session = Depends(get_db)):
    stmt = text("""
        SELECT * FROM emails 
        WHERE MATCH(subject, body) AGAINST(:query IN NATURAL LANGUAGE MODE)
        LIMIT 10
    """)
    result = db.execute(stmt, {"query": q}).mappings().all()
    return result
