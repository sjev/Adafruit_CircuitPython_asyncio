# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Dan Halbert for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2024 Jev Kuznetsov - ROX Automation
#
# SPDX-License-Identifier: Unlicense

""" simple async example """

import asyncio


async def loop(id: int, delay: float = 0.1):
    """print (i+1) dots"""
    for i in range(5):
        print(f"loop {id} : " + (i + 1) * ".")
        await asyncio.sleep(delay)
    print(f"loop {id} : done")


async def main():
    coros = [loop(1), loop(2, 0.5), loop(3, 1.0)]
    await asyncio.gather(*coros)


asyncio.run(main())
