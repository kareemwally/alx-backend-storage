#!/usr/bin/env python3
"""
a simple module to deal with redis by sending data
in form of Key(bytes) :value(any data)
"""
import redis
import uuid
from typing import Union
annotations = Union[str, bytes, int, float]


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

    def get_int(self, key):
        """
        the fn is integer
        it returns data in int format
        """
        return self.get(key, fn=int)

    def get_str(self, key):
        """
        the fn is str
        it returns data in str format
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get(self, key: str, fn: callable) -> annotations:
        """
        getting the data the way fn is
        """
        if key is None:
            return None
        if fn is None:
            return self._redis.get(key)
        else:
            return fn(self._redis.get(key))
