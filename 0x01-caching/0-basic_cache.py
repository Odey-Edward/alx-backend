#!/usr/bin/env python3
"""BasicCache Module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class for basic caching"""

    def __init__(self):
        """BasicCache initialization method"""
        super().__init__()

    def put(self, key, item):
        """insert item to the cache storage"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """retrive item from the cache storage"""
        if key in self.cache_data:
            return self.cache_data[key]

        return None
