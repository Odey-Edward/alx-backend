#!/usr/bin/env python3
"""FIFOCache Module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache Class that implement the Fifocache replacement
    replacement policies"""

    def __init__(self):
        """FIFOCache class initialization method"""
        super().__init__()

    def put(self, key, item):
        """insert item to the cache storage"""
        if key and item:
            if len(self.cache_data.values()) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                oldest_key = min(self.cache_data.keys())
                del self.cache_data[oldest_key]
                self.cache_data[key] = item
                print('DISCARD: {}'.format(oldest_key))

    def get(self, key):
        """retrive item from the cache storage"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
