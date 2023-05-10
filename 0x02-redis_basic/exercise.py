#!/usr/bin/env python3
'''
Project on Redis basics
'''


import redis
from typing import Union
from uuid import uuid4, UUID


class Cache:
    ''' Class for implementing a Cache with redis '''

    def __init__(self):
        ''' Constructor '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        store the input data in Redis using a random key
        and return the key
        '''
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
