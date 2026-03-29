from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
class CodeHistory(Base):
    __tablename__ = "code_history"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(Text)
    language = Column(String)
    result = Column(Text)
    user_email = Column(String)