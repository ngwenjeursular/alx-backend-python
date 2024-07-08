#!/usr/bin/env python3
# 0-basic_async_syntax.py

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
	"""
	Wait for a random delay between 0 and max_delay seconds
        and return the delay.
	"""
	# Generate a random delay
	delay = random.uniform(0, max_delay)
	# Wait for the delay
	await asyncio.sleep(delay)
	# Return the delay
	return delay
