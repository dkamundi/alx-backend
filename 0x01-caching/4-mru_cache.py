#!/usr/bin/env python3
""" MRUCache module
"""
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache defines a caching system using the Most Recently Used (MRU) algorithm.
    """

    def __init__(self):
        """ Initialize the caching system.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using MRU algorithm.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the most recently used item (MRU) when the cache is full
                mru_key = self.order.pop()
                print(f"DISCARD: {mru_key}")
                del self.cache_data[mru_key]

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item from the cache by key.
        """
        if key is not None:
            if key in self.order:
                # Move the accessed key to the end of the order to mark it as most recently used
                self.order.remove(key)
                self.order.append(key)
            return self.cache_data.get(key)
