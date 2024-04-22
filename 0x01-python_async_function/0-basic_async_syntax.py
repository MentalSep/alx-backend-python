#!/usr/bin/env python3
"""Model for task 0"""
from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay and returns it."""
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
