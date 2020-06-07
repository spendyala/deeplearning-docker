from aiohttp import ClientSession
from aiohttp.client_exceptions import *

import aiohttp
import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def fetch_1(session, asyncState):
    try:
        url = 'https://www.google.com'
        async with session.get(url) as response:
            print(f'Received the response for URL {url}.'
                  f' Response status {response.status}')
            return response.url, response.status, await response.text(),
    except ClientConnectorError as err:
        return url, -1, {'code': 99999,
                         'message': 'Connection Error {}'.format(err.__dict__)}

async def fetch_2(session, asyncState):
    try:
        print('Here in fetch_2')
        url = 'https://www.google.com'
        async with session.get(url) as response:
            raise Exception('Hello!')
            print(f'Received the response for URL {url}.'
                  f' Response status {response.status}')
            asyncState.http_flag_2 = False
            return response.url, response.status, await response.text(),
    except ClientConnectorError as err:
        return url, -1, {'code': 99999,
                         'message': 'Connection Error {}'.format(err.__dict__)}
    except Exception as err:
        print(err.__dict__)
        asyncState.http_flag_2 = True

async def fetch_3(session, asyncState):
    print(f'Here in fetch_3 {asyncState.http_flag_2}')
    while asyncState.http_flag_2 is None:
        await asyncio.sleep(0.005)
        if asyncState.http_flag_2 in [True, False]:
            break
    print(f'Out of while in fetch_3 {asyncState.http_flag_2}')
    if asyncState.http_flag_2 is False:
        print('Request processed.')
        return
    print(f'Processing of while in fetch_3 {asyncState.http_flag_2}')
    try:
        url = 'https://www.google.com'
        async with session.get(url) as response:
            raise Exception('Hello')
            print(f'Received the response for URL {url}.'
                  f' Response status {response.status}')
            return response.url, response.status, await response.text(),
    except ClientConnectorError as err:
        return url, -1, {'code': 99999,
                         'message': 'Connection Error {}'.format(err.__dict__)}
    except Exception as err:
        asyncState.http_flag_2 = True



async def my_timer_05():
    count = 0
    while True:
        count += 1
        if count > 100:
            break
        await asyncio.sleep(0.005)
        print('Run my timer 1 {}'.format(count))


async def my_timer_2(asyncState):
    count = 0
    while asyncState.timer_flag_1:
        count += 1
        if count > 10:
            asyncState.timer_flag_1 = False
        await asyncio.sleep(2)
        print('Run my timer 2 {}'.format(count))


async def main():
    tasks = []
    asyncState = type('', (), {})() # Empty Object 
    asyncState.http_flag_1 = False
    asyncState.http_flag_2 = None
    # asyncState.timer_flag_1 = True
    async with ClientSession() as session:
        # tasks.append(asyncio.ensure_future(my_timer_05()))
        # tasks.append(asyncio.ensure_future(my_timer_2(asyncState)))
        tasks.append(asyncio.ensure_future(fetch_1(session, asyncState)))
        tasks.append(asyncio.ensure_future(fetch_2(session, asyncState)))
        tasks.append(asyncio.ensure_future(fetch_3(session, asyncState)))
        await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
try:
    # loop.run_forever()
    loop.run_until_complete(main())
except KeyboardInterrupt:
    pass
finally:
    print('Closing loop.')
    loop.close()
