from aiohttp import ClientSession
from aiohttp.client_exceptions import *

import aiohttp
import asyncio
import socket
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def fetch_1(session, asyncState):
    try:
        url = 'http://example.com/some/redirect/'
        # import ipdb; ipdb.set_trace()
        async with session.get(url) as response:
            print(f'Received the response for URL {url}.'
                  f' Response status {response.status}')
            # print(response.history)
            # print(response.history[1])
            return response.url, response.status, await response.text(),
    except ClientConnectorError as err:
        return url, -1, {'code': 99999,
                         'message': 'Connection Error {}'.format(err.__dict__)}


async def fetch_2(session, asyncState, loop):
    try:
        url = 'google.com'
        # import ipdb; ipdb.set_trace()
        target = (url,'https')
        info = await loop.getaddrinfo(
            *target,
            proto=socket.IPPROTO_TCP,
        )
        print(info)
    except ClientConnectorError as err:
        pass

async def main(loop):
    tasks = []
    asyncState = type('', (), {})() # Empty Object
    asyncState.http_flag_1 = False
    asyncState.http_flag_2 = None
    # asyncState.timer_flag_1 = True
    async with ClientSession() as session:
        tasks.append(asyncio.ensure_future(fetch_1(session, asyncState)))
        tasks.append(asyncio.ensure_future(fetch_2(session, asyncState, loop)))
        await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
try:
    # loop.run_forever()
    loop.run_until_complete(main(loop))
except KeyboardInterrupt:
    pass
finally:
    print('Closing loop.')
    loop.close()
