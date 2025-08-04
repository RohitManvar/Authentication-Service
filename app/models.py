from app.db import collections
from bson import ObjectId
from datetime import datetime
from pymongo.errors import DuplicateKeyError
import logging

async def get_user_by_username(username: str):
    try:
        return await collections.find_one({"username": username})
    except Exception as e:
        logging.error(f"Database error getting user: {e}")
        return None

async def create_user(username: str, password: str):
    try:
        user_doc = {
            "username": username,
            "password": password,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        result = await collections.insert_one(user_doc)
        return str(result.inserted_id)
    except DuplicateKeyError:
        raise ValueError("Username already exists")
    except Exception as e:
        logging.error(f"Database error creating user: {e}")
        raise
