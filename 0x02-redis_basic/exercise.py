#!/usr/bin/env python3
"""
a simple module to deal with redis by sending data
in form of Key(bytes) :value(any data)
"""
import redis
import uuid
from typing import Union, Any, Optional, Callable
annotations = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    Uses the method's qualified name as the key in Redis.
    Args:
        method: The method to be decorated
    Returns:
        Callable: The wrapped method that counts calls
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the counter
        and calls the method
        """
        # Increment the counter using the method's qualified name
        self._redis.incr(method.__qualname__)
        # Call and return the original method
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    the base class of the cashing system in project
    """
    def __init__(self):
        """
        instiating the connection with redis server on localhost
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: annotations) -> str:
        """
        storing the specifed data whether it's int or float or string
        or bytes
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
