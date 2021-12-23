import fastapi
import redis

from paji.dependencies import get_config


def get_jessiclient_config(config=fastapi.Depends(get_config)):
    return config.services.jessiclient


def get_redis_client(config=fastapi.Depends(get_config)):
    redis_client = redis.Redis(
        host=config.cache.redis.host,
        port=config.cache.redis.port,
    )
    try:
        yield redis_client
    finally:
        redis_client.close()
