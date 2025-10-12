import aiohttp
import asyncio
from ccxt.async_support import binance

async def test_binance():
    proxy = "http://127.0.0.1:7890"
    async with binance({"aiohttp_proxy": proxy}) as exchange:
        markets = await exchange.load_markets()
        print(markets)

asyncio.run(test_binance())

