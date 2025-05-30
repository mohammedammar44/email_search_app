from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import Base

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String(255))
    recipient = Column(String(255))
    subject = Column(Text)
    body = Column(Text)
    sent_at = Column(DateTime)
