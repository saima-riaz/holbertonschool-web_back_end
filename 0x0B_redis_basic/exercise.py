#!/usr/bin/env python3
"""
cache class to interact with Redis for storing data
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key and optionally apply a conversion
        function `fn` to the result.
        """
        date = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_srt(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis by key, decoding from bytes to str.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis by key, converting from bytes to int.
        """
        return self.get(key, fn=int)
