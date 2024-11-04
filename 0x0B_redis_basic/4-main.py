# main.py
from exercise import Cache, replay

# Create an instance of Cache
cache = Cache()

# Store some values
cache.store("foo")
cache.store("bar")
cache.store(42)

# Display the history of calls to the store method
replay(cache.store)
