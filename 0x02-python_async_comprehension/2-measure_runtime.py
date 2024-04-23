#!/usr/bin/env python3
"""Module for measuring runtime"""
import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of async_comprehension called 4 times."""
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = perf_counter()

    return end_time - start_time
