#!/usr/bin/python3
""" LRU caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if key in self.key_order:
            self.key_order.remove(key)

        self.key_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.key_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.key_order:
            return None
         
         # Move the key to the most recently used position
        self.key_order.remove(key)
        self.key_order.append(key)

        return self.cache_data[key]

        