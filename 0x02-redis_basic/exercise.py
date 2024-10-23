#!/usr/bin/env python3
"""
a simple module to deal with redis by sending data
in form of Key(bytes) :value(any data)
"""
import redis
import uuid
from typing import Union


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

    def store(self, data: Union[int, float, str, bytes]) -> set:
        """
        storing the specifed data whether it's int or float or string
        or bytes
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
