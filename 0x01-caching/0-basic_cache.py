#!/usr/bin/python3
"""
    BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):

    '''
        BasicCache is a caching system inherit
        from BaseCaching class
    '''

    MAX_ITEMS = None

    def __init__(self):
        '''
            Inherit the cache data from parent class
        '''
        super().__init__()

    def put(self, key, item):
        '''
            Add an item to the cache
        '''
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''
            Get an item from the cache
        '''
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
