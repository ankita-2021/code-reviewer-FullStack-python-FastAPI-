from pydantic import BaseModel
from typing import List, Literal

class CodeReviewRequest(BaseModel):
    code: str
    language: Literal['python', "java", "cpp"]
    
class CodeReviewResponse(BaseModel):
    review: str
    detected_patterns: List[str]
    mistakes: List[str]
    time_complexity: str
    space_complexity: str
    optimizations: List[str]
    dsa_suggestion: List[str]
    interview_questions: List[str]
    
class UserCreate(BaseModel):
    name: str
    email: str
    password : str
    
class UserLogin(BaseModel):
    email: str
    password: str
        

        