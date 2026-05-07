import bcrypt
from datetime import datetime, timedelta    
from jose import JWTError, jwt  
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "clave_secreta_123"
ALGORITHM = "HS256" 
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/usuarios/login")

def _normalize_password(password: str) -> bytes:
    if isinstance(password, str):
        password = password.encode('utf-8')
    if len(password) > 72:
        raise ValueError('Password cannot be longer than 72 bytes')
    return password


def hash_password(password: str) -> str:
    normalized = _normalize_password(password)
    hashed = bcrypt.hashpw(normalized, bcrypt.gensalt())
    return hashed.decode('utf-8')

def verify_password(plain_password, hashed_password): 
    try:
        normalized = _normalize_password(plain_password)
        return bcrypt.checkpw(normalized, hashed_password.encode('utf-8'))
    except (ValueError, TypeError):
        return False

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload["sub"]

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})   
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):  
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:    
        return None
