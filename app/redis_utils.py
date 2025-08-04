import redis.asyncio as redis
import logging

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

async def store_token(username: str, token: str):
    try:
        await redis_client.set(f"token:{username}", token, ex=900)
        return True
    except Exception as e:
        logging.error(f"Failed to store token in Redis: {e}")
        return False

async def get_token(username: str):
    try:
        return await redis_client.get(f"token:{username}")
    except Exception as e:
        logging.error(f"Failed to get token from Redis: {e}")
        return None

async def delete_token(username: str):
    try:
        await redis_client.delete(f"token:{username}")
        return True
    except Exception as e:
        logging.error(f"Failed to delete token from Redis: {e}")
        return False
