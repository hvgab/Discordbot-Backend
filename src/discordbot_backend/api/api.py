import discord
import logging
import pprint
import asyncio

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

TOKEN = ''

if __name__ == '__main__':
    client = discord.Client()
    asyncio.run(client.login(TOKEN))

    pprint.pprint(client.guilds)
