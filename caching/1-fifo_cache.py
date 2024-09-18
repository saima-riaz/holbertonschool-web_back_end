#!/usr/bin/python3
""" FIFO caching system """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching system that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the class and its attributes """
        super().__init__()
        self.key_order = []  # To track the order of keys (FIFO)

    def put(self, key, item):
        """ Add an item to the cache following FIFO policy """
        if key is None or item is None:
            return

        # Add the key to the order list if it is new
        if key not in self.cache_data:
            self.key_order.append(key)

        
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.key_order.pop(0)  # Remove the oldest key
            del self.cache_data[first_key]     # Delete the oldest item
            print(f"DISCARD: {first_key}")    # Print the discarded key

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key, None)
