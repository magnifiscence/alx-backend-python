#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time with async
"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines at the same time with async

    Args:
        max_delay (int, optional): Maximum delay in seconds (default is 10).
        n (int, optional): Number of times to execute the coroutine
                           (default is 0).

    Returns:
        List[float]: List of actual delays from each coroutine.
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return sorted([await delay for delay in asyncio.as_completed(delays)])
