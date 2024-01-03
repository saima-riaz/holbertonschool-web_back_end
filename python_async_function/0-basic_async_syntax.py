#!/usr/bin/env python3
"""
This Python script defines an asynchronous coroutine 'wait_random'
It takes an integer argument 'max_delay' and returns a random float delay
between 0 and the specified 'max_delay'
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns delay between 0 and max_delay"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
