# Asynchronous Python Scripts - Async and Python

This collection of Python scripts demonstrates asynchronous programming using coroutines and asyncio. The scripts focus on creating random delays, measuring execution time, and utilizing asyncio tasks.

## Contents

1. [**`0-basic_async_syntax.py`**](0-basic_async_syntax.py)
   - Asynchronous coroutine `wait_random` takes an integer argument `max_delay` and returns a random float delay between 0 and `max_delay`.

2. [**`1-concurrent_coroutines.py`**](1-concurrent_coroutines.py)
   - Coroutines `wait_n` takes in an integer `n` and `max_delay`, returning a list of delays in ascending order.

3. [**`2-measure_runtime.py`**](2-measure_runtime.py)
   - Function `measure_time` measures the total execution time for `wait_n(n, max_delay)` and returns the average time.

4. [**`3-tasks.py`**](3-tasks.py)
   - Regular function `task_wait_random` creates an asyncio Task for `wait_random(max_delay)`.

5. [**`4-task_wait_n.py`**](4-task_wait_n.py)
   - Module returns a list of delays using asyncio tasks and `task_wait_random`.
