#!/usr/bin/env python3
""" LIFOCache module
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system using the LIFO algorithm.
    """

    def __init__(self):
        """ Initialize the caching system.
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item to the cache using LIFO algorithm.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the last item (LIFO) when the cache is full
                discarded_key = self.stack.pop()
                print(f"DISCARD: {discarded_key}")
                del self.cache_data[discarded_key]

            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """ Get an item from the cache by key.
        """
        if key is not None:
            return self.cache_data.get(key)
