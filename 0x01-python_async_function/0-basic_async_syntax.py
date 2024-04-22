#!/usr/bin/env python3
"""Model for task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay and returns it."""
    delay = asyncio.uniform(0, max_delay)
    await random.sleep(delay)
    return delay
