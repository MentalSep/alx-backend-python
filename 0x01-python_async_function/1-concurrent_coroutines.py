#!/usr/bin/env python3
"""Model for task 1"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns n wait_random coroutines and returns a list of
    delays in ascending order."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delays = sorted(await asyncio.gather(*tasks))
    return delays
