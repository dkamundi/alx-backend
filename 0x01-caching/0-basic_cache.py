#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a caching system without a limit.
    """

    def put(self, key, item):
        """ Add an item to the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item


    def get(self, key):
        """ Get an item from the cache by key.
        """
        if key is not None:
            return self.cache_data.get(key)
