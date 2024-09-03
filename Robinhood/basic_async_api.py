import asyncio

import aiohttp
import multidict
import ujson


class ApiOperations:
    def __init__(self):
        self.session = None
        self.default_header = multidict.CIMultiDict({})

    async def initialize(self):
        if self.session is None:
            self.session = aiohttp.ClientSession(
                headers=self.default_header, json_serialize=ujson.dumps
            )

    async def close(self):
        if self.session:
            await self.session.close()

    async def async_get_wild(self, url, params=None, headers=None, jsonify_data=False):
        if self.session is None:
            await self.initialize()
        async with self.session.get(
            url, params=params, headers=headers, ssl=False
        ) as resp:
            if jsonify_data:
                try:
                    response = await resp.json()
                except aiohttp.client_exceptions.ContentTypeError as err:
                    print(err)
                    print(await resp.text())
                    raise
            else:
                response = await resp.text()
            return response

    async def async_post_wild(
        self, url, payload, params=None, headers=None, jsonify_data=False
    ):
        if self.session is None:
            await self.initialize()
        async with self.session.post(
            url, params=params, data=payload, headers=headers, ssl=False
        ) as resp:
            if jsonify_data:
                resp = await resp.json()
            else:
                resp = await resp.text()
            return resp

    async def async_delete(self, url, headers, payload):
        if self.session is None:
            await self.initialize()
        async with self.session.delete(
            url, headers=headers, data=payload, ssl=False
        ) as resp:
            json_resp = await resp.json()
            return json_resp
