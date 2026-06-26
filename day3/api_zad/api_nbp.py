import asyncio
import aiohttp
import time

# httpx

# https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/
url = "https://api.nbp.pl/api/exchangerates/rates/A/eur/"


async def fetch(url, session, index):
    async with session.get(url, ssl=False) as response:
        text = await response.text()
        print(f"Text: {text}")
