#!/usr/bin/env python3
""" LRUCache module
"""
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ LRUCache defines a caching system using the Least Recently Used (LRU) algorithm.
    """

    def __init__(self):
        """ Initialize the caching system.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using LRU algorithm.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the least recently used item (LRU) when the cache is full
                lru_key = self.order.pop(0)
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]

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
