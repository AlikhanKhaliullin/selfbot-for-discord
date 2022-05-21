import requests
import asyncio
import discord
from discord.ext import commands
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime, date, time
from discord.ext import commands
from datetime import datetime, timedelta
from io import BytesIO
from discord.utils import get
import sys

sys.path.insert(0, 'selfbot-for-discord/src')
import config 
from  bot import Main
#from monitore import keep_alive


bot = commands.Bot(command_prefix="7", intents=discord.Intents.all(), self_bot = True)


@bot.command(pass_context = True) 
async def flash(ctx, *args):
    await ctx.send(' '.join(args))
    await ctx.message.add_reaction("❤️")
    with open("music.txt", "w") as f:
        f.write(' '.join(args))


bot.run(config.karami, bot = False)