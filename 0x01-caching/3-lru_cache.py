#!/usr/bin/env python3
"""LRUCache Module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Class that implements the LRU cache
    replacement policy"""

    def __init__(self):
        """LRUCache class initialization method"""
        super().__init__()
        self.__usage_tracker = {}
        self.__usage_counter = 0

    def put(self, key, item):
        """insert item to the cache storage"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least recently used key to evict
                lru_key = min(self.__usage_tracker,
                              key=self.__usage_tracker.get)
                del self.cache_data[lru_key]
                del self.__usage_tracker[lru_key]

                if key != lru_key:
                    print('DISCARD: {}'.format(lru_key))

            self.cache_data[key] = item
            self.__usage_tracker[key] = self.__usage_counter
            self.__usage_counter += 1

    def get(self, key):
        """retrieve item from the cache storage"""
        if key in self.cache_data:
            self.__usage_tracker[key] = self.__usage_counter
            self.__usage_counter += 1
            return self.cache_data[key]
        return None
