#!/usr/bin/env python3
"""Tasks"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Tasks

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        asyncio.Task: asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
