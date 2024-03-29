from discord.ext import tasks
from discord.ext import commands
import time
from utils import get_or_fetch_channel
import aiohttp

class Scraper(commands.Cog, command_attrs=dict(hidden=False)):
    def __init__(self, bot):
        self.bot = bot 
        self.scrape.start()

    @tasks.loop(seconds=10.0)
    async def scrape(self):
        if self.bot.doScrape is True:
            async with aiohttp.ClientSession() as session:
                async with session.get('http://142.202.220.236:8123/up/world/world/1') as resp:
                    text = await resp.text()
                    ch = await get_or_fetch_channel(self, 994478862362759188)
                    if '\"isThundering\":true' in text:
                        if self.bot.currentlyThundering is False:
                            await ch.send(f"everyone a thunderstorm started <t:{int(time.time())}:R>")
                            self.bot.currentlyThundering = True
                    else:
                        if self.bot.currentlyThundering is True:
                            await ch.send("The thunderstorm has stopped...")
                            self.bot.currentlyThundering = False

                    errorCH = await get_or_fetch_channel(self, self.bot.errorCH)
                    await errorCH.send(f"last updated <t:{int(time.time())}:R>\nCurrently Thundering: {self.bot.currentlyThundering}", delete_after=10)



    @scrape.before_loop
    async def wait(self):
        await self.bot.wait_until_ready()


def setup(bot):
	bot.add_cog(Scraper(bot))