#!/usr/bin/env python3
"""Model for task 4"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn n task_wait_random coroutines with the specified max_delay"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = sorted(await asyncio.gather(*tasks))
    return delays
