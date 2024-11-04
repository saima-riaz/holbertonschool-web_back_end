# test_exercise.py

from exercise import Cache

# Create a Cache instance
cache = Cache()

# Define test cases
TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

# Run tests
for value, fn in TEST_CASES.items():
    key = cache.store(value)
    # Assert that the retrieved value matches the original input value
    assert cache.get(key, fn=fn) == value, f"Test failed for value: {value}"

print("All tests passed.")
