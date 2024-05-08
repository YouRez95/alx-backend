#!/usr/bin/python3
"""
    LRUCache module
"""
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    '''
       LRUCache is a caching algorithm
       that evict the least recently used
       and keep the most recently used
    '''

    def __init__(self):
        '''
            Inherit the cache data from parent class
        '''
        super().__init__()
        self.tracking = []

    def put(self, key, item):
        '''
            Add an item to the cache
        '''
        if not key or not item:
            return
        if self.MAX_ITEMS == len(self.tracking):
            evicted = self.tracking[0]
            del self.cache_data[evicted]
            if key not in self.tracking:
                print('DISCARD: {}'.format(evicted))
            for i in range(0, self.MAX_ITEMS):
                if i + 1 < self.MAX_ITEMS:
                    self.tracking[i] = self.tracking[i + 1]
                else:
                    self.tracking[i] = key
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item
            self.tracking.append(key)

    def get(self, key):
        '''
            Get an item from the cache
        '''
        if not key or key not in self.cache_data:
            return None
        # self.tracking.
        index = self.tracking.index(key)
        for i in range(index, self.MAX_ITEMS):
            if i + 1 < self.MAX_ITEMS:
                self.tracking[i] = self.tracking[i + 1]
        self.tracking[self.MAX_ITEMS - 1] = key
        return self.cache_data[key]
