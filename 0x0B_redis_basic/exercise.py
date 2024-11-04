#!/usr/bin/env python3
"""
cache class to interact with Redis for storing data
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """initialize Redis client and flush database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key,store data in Redisusing keys
        and return key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
