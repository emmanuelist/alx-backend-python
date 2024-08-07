#!/usr/bin/env python3
"""
Module for measuring the runtime of executing multiple async comprehensions
concurrently.

This module provides a single function, `measure_runtime`,
which creates a list of tasks, each executing the `async_comprehension`
function, and then uses `asyncio.gather` to run them concurrently.
The time it takes to complete all tasks is measured using `time.perf_counter`.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of executing multiple async
    comprehensions concurrently.

    This function creates a list of tasks, each executing the
    `async_comprehension` function,
    and then uses `asyncio.gather` to run them concurrently.
    The time it takes to complete
    all tasks is measured using `time.perf_counter`.

    Returns:
        float: The total runtime in seconds.
    """
    t_start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)
