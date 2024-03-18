#!/usr/bin/env python3
"""The basics of async"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that introduces a random delay.

    Args:
        max_delay (int, optional): Maximum delay in seconds (default is 10).

    Returns:
        float: Random delay between 0 and max_delay (inclusive).
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
