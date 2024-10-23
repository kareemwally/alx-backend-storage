#!/usr/bin/env python3
"""
A simple module to deal with redis by sending data
in form of Key(bytes) : value(any data)
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps

RedisValue = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    Uses the method's qualified name as the key in Redis.
    """
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the counter
        and calls the method
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    The base class of the caching system in project.
    Handles storage and retrieval of data with type conversion support.
    """
    def __init__(self):
        """
        Instantiating the connection with redis server on localhost
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: RedisValue) -> str:
        """
        Store the specified data whether
        it's int, float, string or bytes.

        This method's calls are counted using the count_calls
        decorator.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieve data from Redis and
        optionally convert it using the provided function.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn is not None else value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis.
        """
        return self.get(key, fn=int)
