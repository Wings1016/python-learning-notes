#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import time

async def get(s, i):
    start = time.time()
    async with s.get('https://www.baidu.com') as r:
        await r.read()
    print(i, ': {} s'.format(round(time.time() - start, 2)))


async def test():
    async with aiohttp.ClientSession(trust_env=True) as s:
        # 经测试加上trust_env参数速度会快一点
        await asyncio.gather(*[get(s, i) for i in range(10)])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())