import aiohttp


async def get(url: str, params: dict) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:

            return await resp.json()
