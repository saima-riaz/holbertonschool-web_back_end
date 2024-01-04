#!/usr/bin/env python3
"""Define a coroutine named async_comprehension that takes no arguments"""

from asyncio import sleep
from random import uniform
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """An asynchronous comprehension that uses the async_generator coroutine"""
    a = [i async for i in async_generator()]
    return a
