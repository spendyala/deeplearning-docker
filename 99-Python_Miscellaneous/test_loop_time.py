import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    print(loop.time())
    end_time = loop.time() + 5.0
    print(end_time)
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())
