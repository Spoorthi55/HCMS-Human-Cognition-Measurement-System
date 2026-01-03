from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from db import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    concept = Column(String)
    question = Column(String)
    answer = Column(String)
    explanation = Column(String)
    confidence = Column(Integer)
    time_taken = Column(Float)
    correct = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
