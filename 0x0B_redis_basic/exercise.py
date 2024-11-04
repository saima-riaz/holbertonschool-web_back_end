import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that stores the history of inputs and outputs of a method."""
    @wraps(method)
    def wrapper(self, *args):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        result = method(self, *args)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method: Callable):
    """Display history of calls of a particular function."""
    method_name = method.__qualname__
    redis_instance = method.__self__._redis
    call_count = int(redis_instance.get(method_name) or 0)
    print(f"{method_name} was called {call_count} times:")

    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"
    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    for input_data, output_data in zip(inputs, outputs):
        print(
            f"{method_name}(*{input_data.decode('utf-8')}) -> "
            f"{output_data.decode('utf-8')}"
        )


class Cache:
    def __init__(self):
        """Initialize Redis client and flush database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key,
        store the data in Redis using the key, and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis by
        key and optionally apply a conversion function `fn`."""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis by key, decoding from bytes to str."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from
        Redis by key, converting from bytes to int."""
        return self.get(key, fn=int)
