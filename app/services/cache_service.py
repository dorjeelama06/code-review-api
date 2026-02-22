import hashlib
import redis
import json
from app.config import get_settings

settings = get_settings()
client = redis.from_url(settings.redis_url)

def get_diff(diff: str):
  key = hashlib.md5(diff.encode()).hexdigest()
  result = client.get(key)
  return json.loads(result) if result else None


def set_diff(diff: str, result: dict):
  key = hashlib.md5(diff.encode()).hexdigest()
  client.set(key, json.dumps(result), ex=3600)