#!/usr/bin/python3
"""
    MRUCache module
"""
from base_caching import BaseCaching
from collections import deque


class MRUCache(BaseCaching):
    '''
       MRUCache is a caching algorithm
       that evict the most recently used
       and keep the least recently used
    '''

    def __init__(self):
        '''
            Inherit the cache data from parent class
        '''
        super().__init__()
        self.tracking = deque()

    def put(self, key, item):
        '''
            Add an item to the cache
        '''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            index = self.tracking.index(key)
            self.swap(index)

        if key not in self.cache_data:
            if len(self.tracking) == self.MAX_ITEMS:
                evicted_key = self.tracking.popleft()
                print("DISCARD: {}".format(evicted_key))
                self.tracking.appendleft(key)
                del self.cache_data[evicted_key]
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item
                self.tracking.appendleft(key)

    def get(self, key):
        '''
            Get an item from the cache
        '''
        if key not in self.tracking:
            return None
        else:
            index = self.tracking.index(key)
            self.swap(index)
        return self.cache_data[key]

    def swap(self, index):
        """
            swap the tracking list
        """
        for i in range(index, 0, -1):
            self.tracking[i], self.tracking[i - 1] = \
                self.tracking[i - 1], self.tracking[i]
