#!/usr/bin/env python3
"""
Importing the wait_random from the
0-basic_async_syntax module
the random module
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    Asynchronous coroutine that takes in two integer arguments
    (n and max_delay, with default values of 0 and 10, respectively)
    named wait_n that spawns wait_random n times with the specified
    max_delay.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
