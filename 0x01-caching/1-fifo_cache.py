#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache defines a caching system using the FIFO algorithm.
    """

    def __init__(self):
        """ Initialize the caching system.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item to the cache using FIFO algorithm.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the first item (FIFO) when the cache is full
                discarded_key = self.queue.pop(0)
                print(f"DISCARD: {discarded_key}")
                del self.cache_data[discarded_key]

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item from the cache by key.
        """
        if key is not None:
            return self.cache_data.get(key)

