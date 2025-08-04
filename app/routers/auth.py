from fastapi import APIRouter, HTTPException, status
from app import schemas, auth, models, redis_utils
import logging

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: schemas.UserCreate):
    try:
        
        existing_user = await models.get_user_by_username(user.username)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Username already exists"
            )
        
        
        if len(user.password) < 6:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must be at least 6 characters long"
            )
        
        
        hashed_password = auth.hash_password(user.password)
        user_id = await models.create_user(user.username, hashed_password)
        
        return {
            "msg": "User registered successfully",
            "user_id": user_id,
            "username": user.username
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Registration error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during registration"
        )

@router.post("/login", response_model=schemas.Token)
async def login_user(user: schemas.LoginUser):
    try:
        
        db_user = await models.get_user_by_username(user.username)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )
        

        if not auth.verify_password(user.password, db_user["password"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )
        
        
        token = auth.create_access_token({"sub": user.username})
        
        
        await redis_utils.store_token(user.username, token)
        
        return {
            "access_token": token,
            "token_type": "bearer"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Login error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during login"
        )

@router.post("/logout")
async def logout_user(user: schemas.LoginUser):
    try:
        await redis_utils.delete_token(user.username)
        return {"msg": "Logged out successfully"}
    except Exception as e:
        logging.error(f"Logout error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during logout"
        )
