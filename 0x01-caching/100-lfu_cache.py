#!/usr/bin/python3
"""
    LRUCache module
"""
from base_caching import BaseCaching
from collections import deque


class LFUCache(BaseCaching):
    '''
       LFUCache is a caching algorithm that remove
       the least frequently used element by LRU
    '''

    def __init__(self):
        '''
            Inherit the cache data from parent class
        '''
        super().__init__()
        self.tracking = {1: deque()}

    def put(self, key, item):
        '''
            Add an item to the cache
        '''
        if key is None or item is None:
            return
        exist = False
        for frequency in list(self.tracking.keys()):
            if key in self.tracking[frequency]:
                exist = True
                if frequency + 1 not in list(self.tracking.keys()):
                    self.tracking[frequency + 1] = deque()
                self.tracking[frequency].remove(key)
                self.tracking[frequency + 1].appendleft(key)
                self.clean_tracking(frequency)
                self.cache_data[key] = item
                break
        if not exist:
            if len(list(self.cache_data.keys())) == self.MAX_ITEMS:
                least_frequency = sorted(self.tracking.keys())[0]
                evicted_key = self.tracking[least_frequency].pop()
                self.clean_tracking(least_frequency)
                print("DISCARD:", evicted_key)
                del self.cache_data[evicted_key]
            if 1 not in list(self.tracking.keys()):
                self.tracking[1] = deque()
            self.tracking[1].appendleft(key)
            self.cache_data[key] = item

    def get(self, key):
        '''
            Get an item from the cache
        '''
        if key not in self.cache_data.keys():
            return None
        for frequency in list(self.tracking.keys()):
            if key in self.tracking[frequency]:
                if frequency + 1 not in list(self.tracking.keys()):
                    self.tracking[frequency + 1] = deque()
                self.tracking[frequency].remove(key)
                self.tracking[frequency + 1].appendleft(key)
                self.clean_tracking(frequency)
        return self.cache_data[key]

    def clean_tracking(self, frequency):
        '''
            clean the tracking data
        '''
        if not self.tracking[frequency]:
            self.tracking.pop(frequency)
