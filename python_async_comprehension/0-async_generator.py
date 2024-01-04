#!/usr/bin/env python3
"""Define a coroutine named async_generator that takes no arguments"""

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """An asynchronous generator that yields random floats """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
