#!/usr/bin/python3
"""
    LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
       LIFOCache is a class for caching
       use the LIFO data structure
    '''

    def __init__(self):
        '''
            Inherit the cache data from parent class
        '''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''
            Add an item to the cache
        '''
        if not key or not item:
            return
        if self.MAX_ITEMS <= len(self.queue) and key not in self.cache_data:
            deleted_key = self.queue.pop()
            del self.cache_data[deleted_key]
            print('DISCARD: {}'.format(deleted_key))
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        '''
            Get an item from the cache
        '''
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
