#!/usr/bin/python3
""" LIFO caching system """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

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
            last_key = self.key_order.pop(-2)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item from the cache """
        return self.cache_data.get(key, None)
