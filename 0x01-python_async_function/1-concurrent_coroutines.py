#!/usr/bin/env python3
"""
execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    Return the list of all delays in ascending order.	
    """
    # Create a list of wait_random coroutines
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Run the coroutines concurrently and collect their results
    delays = await asyncio.gather(*tasks)
    # Return the delays sorted in ascending order
    return sorted(delays)
