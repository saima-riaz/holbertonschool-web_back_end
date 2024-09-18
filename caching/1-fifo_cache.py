#!/usr/bin/python3
""" FIFO caching system """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the class and its attributes """
        super().__init__()
        self.key_order = [] # To keep track of insertion order (FIFO)

    def put(self, key, item):
        """ Add an item to the cache following FIFO policy """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.key_order.append(key) # if key is not then add key in the last(track order)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.key_order.pop(0) # Remove the oldest key by using pop
            del self.cache_data[first_key] # Delete the oldest item
            print(f"DISCARD: {first_key}") # print the discard keys

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key, None)
