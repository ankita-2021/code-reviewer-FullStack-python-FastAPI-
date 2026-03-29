from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import CodeReviewRequest
from app.services import generate_review
from app.database import engine
from app.models import Base

from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas import UserCreate
from app.models import User
from app.database import get_db
from app.services import hash_password
from app.schemas import UserLogin
from app.services import verifiy_password
from app.services import create_access_token
# protected route...
from fastapi import Header
from jose import jwt, JWTError
from app.models import CodeHistory

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)

@app.post("/review-code")
def review_code(
    data: CodeReviewRequest, authorization: str = Header(None, alias="Authorization"), 
    db:Session = Depends(get_db)):
    
    if not authorization or not authorization.startswith("Bearer"):
        return {"error": "Invalid token"}
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
        result =  generate_review(data.code, data.language)
        # save to db 
        history = CodeHistory(
        code=data.code,
        language = data.language,
        result = str(result),
        user_email = user_email
        )
        db.add(history)
        db.commit()
        return result
    except:
        return {"error": "Invalid token"}

Base.metadata.create_all(bind=engine)

@app.get("/history")
def get_history(authorization: str = Header(None, alias="Authorization"),db: Session = Depends(get_db)):
    
    if not authorization or not authorization.startswith("Bearer"):
        return {"error": "Invalid token"}
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
        data = db.query(CodeHistory).filter(
            CodeHistory.user_email == user_email).all()
        return data
    except:
        return {"error": "Invalid Token"}

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # duplicate email checking.........
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        return {"error": "Email already registered"}
    
    hashed_pw = hash_password(user.password)
    
    new_user = User(
        name = user.name,
        email = user.email,
        password = hashed_pw
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User created successfully"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    
    if not db_user:
        return {"error": "User not found"}
    if not verifiy_password(user.password, db_user.password):
        return {"error": "wrong password"}
    token = create_access_token({"sub": db_user.email})
    
    return {"message": "Login successful",
            "access_token":token}



SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

@app.get("/protected")
def protected(authorization: str = Header(None, alias="Authorization")):
    try:
        if not authorization:
            return {"error": "Invalid Header format"}

        authorization = authorization.strip()

        if not authorization.lower().startswith("bearer "):
            return {"error": "Invalid Header format"}

        parts = authorization.split(" ")
        if len(parts) != 2:
            return {"error": "Invalid Header format"}

        token = parts[1]

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": "Access granted", "user": payload}

    except JWTError as e:
        print("JWT ERROR:", e)
        return {"error": "Invalid Token"}
    