
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt
from typing import Optional
import os

router = APIRouter()

SECRET = os.getenv('SECRET_KEY', 'changemeplease')

class UserIn(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

@router.post('/login', response_model=Token)
async def login(u: UserIn):
    # NOTE: This is a placeholder. Replace with real user verification and DB.
    if u.username == 'admin' and u.password == 'password':
        payload = {'sub': u.username, 'exp': datetime.utcnow() + timedelta(hours=8)}
        token = jwt.encode(payload, SECRET, algorithm='HS256')
        return {'access_token': token}
    raise HTTPException(status_code=401, detail='Invalid credentials')
