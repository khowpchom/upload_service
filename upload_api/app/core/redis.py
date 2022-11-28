
import redis.asyncio as redis
from .config import settings

redis = redis.from_url(settings.REDIS_URL, decode_responses=True)