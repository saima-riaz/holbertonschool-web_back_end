#!/usr/bin/python3

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.key_order = []
    
    def put(self, key, item):
        if key is None and item is None:
            return
        if key not in self.cache_data:
            self.key_order.append(key)
        
            self.cache_data[key] = item
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.key_order.pop(0)
            del self.cache_data[first_key]
            print (f"DISCARD: {first_key}")
    
    def get(self, key):
        return self.cache_data.get(key, None)