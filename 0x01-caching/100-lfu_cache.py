#!/usr/bin/env python3
"""LFUCache Module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache Class that implements the LFU cache
    replacement policy"""

    def __init__(self):
        """LFUCache class initialization method"""
        super().__init__()
        self.__usage_tracker = {}
        self.__usage_counter = {}
        self.__counter = 0

    def lfu(self):
        """Find keys with the minimum usage frequency"""
        min_frequency = min(self.__usage_counter.values())
        return [key for key, val in self.__usage_counter.items()
                if val == min_frequency]

    def put(self, key, item):
        """Insert item to the cache storage"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = self.lfu()
                if len(lfu_keys) > 1:
                    # Find the least recently used key to evict
                    lfu_key = min(lfu_keys, key=lambda k:
                                  self.__usage_tracker[k])
                else:
                    lfu_key = lfu_keys[0]

                del self.cache_data[lfu_key]
                del self.__usage_tracker[lfu_key]
                del self.__usage_counter[lfu_key]

                if key != lfu_key:
                    print('DISCARD: {}'.format(lfu_key))

            self.cache_data[key] = item
            self.__usage_tracker[key] = self.__counter
            self.__usage_counter[key] = 1
            self.__counter += 1

    def get(self, key):
        """Retrieve item from the cache storage"""
        if key in self.cache_data:
            self.__usage_counter[key] += 1
            self.__usage_tracker[key] = self.__counter
            self.__counter += 1
            return self.cache_data[key]
        return None
