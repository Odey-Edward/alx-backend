#!/usr/bin/env python3
"""LIFOCache Module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class that implement the Lifocache
    replacement policies"""

    def __init__(self):
        """LIFOCache class initialization method"""
        super().__init__()

    def put(self, key, item):
        """insert item to the cache storage"""
        if key and item:
            if len(self.cache_data.values()) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
            else:
                newest_key = max(self.cache_data.keys())
                del self.cache_data[newest_key]
                self.cache_data[key] = item
                print('DISCARD: {}'.format(newest_key))

    def get(self, key):
        """retrive item from the cache storage"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
