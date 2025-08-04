from pydantic import BaseModel, validator
from typing import Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    
    @validator('username')
    def username_must_be_valid(cls, v):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters long')
        if not v.isalnum():
            raise ValueError('Username must contain only letters and numbers')
        return v.lower()
    
    @validator('password')
    def password_must_be_valid(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v

class LoginUser(UserBase):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class User(UserBase):
    id: Optional[str] = None
    created_at: Optional[str] = None
