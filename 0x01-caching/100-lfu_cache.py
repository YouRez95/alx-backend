#!/usr/bin/python3
"""
    LRUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
       MRUCache is a caching algorithm
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
        if key in self.tracking:
            index = self.tracking.index(key)
            for i in range(index, self.MAX_ITEMS):
                if i + 1 < self.MAX_ITEMS:
                    self.tracking[i] = self.tracking[i + 1]
            return
        if self.MAX_ITEMS == len(self.tracking):
            evicted = self.tracking.pop()
            print('DISCARD: {}'.format(evicted))
            self.tracking.append(key)
            del self.cache_data[evicted]
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
