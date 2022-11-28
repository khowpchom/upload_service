import asyncio
import httpx
import timeit
import json

from uuid import UUID
import numpy as np
from io import BytesIO
import pandas as pd
from fastapi import File

from core.redis import redis


async def get_reach_url(url: str) -> bool:
    ssl_prefix = "https://"
    normal_prefix = "http://"
    if (ssl_prefix not in url) and (normal_prefix not in url):
        url = f"{normal_prefix}{url}"
    can_reach = False
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(url, follow_redirects=True, timeout=5)
            if r.status_code == httpx.codes.OK:
                can_reach = True
            else:
                r.raise_for_status()
        except httpx.HTTPError as exc:
            print(f"Error while requesting {exc.request.url!r}.")
    return can_reach

async def task_upload(file: File(...), task_id: UUID) -> None:
    start = timeit.default_timer()
    contents = file.file.read()
    buffer = BytesIO(contents)
    df = pd.read_csv(buffer, header=None, usecols=[0], dtype=str)

    url_list = [url for url in df[0].to_numpy().tolist()]

    total = 0
    up = 0
    for chunk_url in np.array_split(url_list, 4):
        tasks = [get_reach_url(url) for url in chunk_url]
        results = await asyncio.gather(*tasks)
        await redis.incr(f"upload:{task_id}", 25)
    
        total += len(results)
        up += results.count(True)

    buffer.close()
    file.file.close()

    result = {
        "process_time": timeit.default_timer() - start,
        "total": total,
        "up": up,
        "down": total - up
    }
    await redis.set(f"result:{task_id}", json.dumps(result))