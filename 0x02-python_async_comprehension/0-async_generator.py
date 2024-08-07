#!/usr/bin/env python3
"""
A Python module that provides an asynchronous generator to loop 10 times,
yielding random floating point numbers between 0 and 10 with a 1-second pause
between each yield.

This module is useful for demonstrating asynchronous generators and can be
used as a building block for more complex asynchronous applications.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random floating point
    numbers between 0 and 10.

    This generator uses asyncio.sleep to pause execution
    for 1 second between each yield.

    Yields:
        float: A random floating point number between 0 and 10.

    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
