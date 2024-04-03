#!/usr/bin/env python3
"""LRUCache Module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Class that implement the LRU cache
    replacement policy"""

    def __init__(self):
        """LRUCache class initialization method"""
        super().__init__()
        self.__usage_tracker = {}

    def __get_key_by_value(self, d, value):
        """get key from a dict by value"""
        for key, val in sorted(d.items()):
            if val == value:
                return key

    def put(self, key, item):
        """insert item to the cache storage"""
        if key and item:
            if len(self.cache_data.values()) < BaseCaching.MAX_ITEMS:
                if self.__usage_tracker:
                    value = max(self.__usage_tracker.values())
                    self.__usage_tracker[key] = value + 1
                else:
                    self.__usage_tracker[key] = 0

                self.cache_data[key] = item
            else:
                value = min(self.__usage_tracker.values())

                if key not in self.cache_data:
                    k = self.__get_key_by_value(self.__usage_tracker, value)
                    del self.cache_data[k]
                    del self.__usage_tracker[k]

                    print('DISCARD: {}'.format(k))

                value = max(self.__usage_tracker.values())
                self.__usage_tracker[key] = value + 1
                self.cache_data[key] = item

    def get(self, key):
        """retrive item from the cache storage"""
        if key in self.cache_data:
            if key in self.__usage_tracker:
                value = max(self.__usage_tracker.values())
                self.__usage_tracker[key] = value + 1
            return self.cache_data[key]
        return None
