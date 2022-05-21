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
from  bot import Main
import praw
import random
import config 
#from monitore import keep_alive
reddit = praw.Reddit(client_id='pu50VW8kp6T8ow', 
                    client_secret='dVBz_83ykBYG7OO90XRjWFrhYk5UTQ', 
                    user_agent='<console:HAPPY:1.0>')

bot = commands.Bot(command_prefix="7", intents=discord.Intents.all(), self_bot = True)
bot.remove_command("help")
 
zxc = Main(bot)

@bot.event
async def on_ready():
    await zxc.start_bot()

@bot.event
async def on_raw_reaction_add(ctx):
    if (ctx.user_id == 455648658914934785):
        with open("music.txt", "r") as f:

            await zxc.vcconnect(ctx,ctx.member)
            await zxc.downdload_music(f.readlines())
            await zxc.play_music(ctx)

@bot.command()
async def vrf(ctx,sub):
    sub = reddit.subreddit(sub)
    images = [i.url for i in sub.hot(limit=100)]
    await ctx.send(random.choice(images))

def take_image(a):
    return Image.open(BytesIO(requests.get(str(a)).content))

def images_take(link,member1,ctx,member2=None):

    img1 = take_image(link)
    if member2 == None:
        img2 = take_image(ctx.author.avatar_url)
    else: 
        img2 = take_image(member2.avatar_url)
    img3 = take_image(member1.avatar_url)
    return img1, img2, img3

@bot.command(pass_context=True)
async def boku(ctx,member1:discord.Member,member2:discord.Member=None):
    link = "https://cdn.discordapp.com/attachments/505733771325079572/778218755024093214/09b2f8de3da504ba.png"
    img1, img2, img3 = images_take(link,member1,ctx,member2)
    img2 = img2.convert("RGB")
    img3 = img3.convert("RGB")
    img2=img2.resize((53,85))
    img3=img3.resize((70,68))
    img3=img3.rotate(-30)
    bk = Image.new('RGB', (203, 299), (0, 0, 0, 0))
    bk.paste(img2,(80,90))
    bk.paste(img3,(120,30))
    bk.paste(img1,mask=img1)
    bk.save("w.jpg")
    await ctx.channel.send(file=discord.File('w.jpg'))

@bot.command(pass_context=True)
async def pistol(ctx,member:discord.Member=None):
    link ="https://cdn.discordapp.com/attachments/680060167856848947/777925629525229608/153-1533170_aiming-gun-png-transparent-png-download.png"
    img1, img3, img2 = images_take(link,member,ctx)
    img2 = img2.convert("RGB")
    (width, height) = img2.size
    img1=img1.resize((width,height))
    img2.paste(img1,(-80,height//2),mask=img1)
    img2.save("w.jpg")
    await ctx.channel.send(file=discord.File('w.jpg'))



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.invisible)


@bot.command(pass_context = True) 
async def clear(ctx,count):
    await clear_message(ctx,count=count)


@bot.command(pass_context = True)
async def vcmute(ctx, member: discord.Member, switch: bool):
    await clear_message(ctx)
    await member.edit(mute = switch) 
    
@bot.command(pass_context = True)
async def flash(ctx, *arg):
    print(arg)
    
    
    #await zxc.vcconnect(ctx,member)
    #path="/song2.mp3"
    #await zxc.play_music(ctx,path)

    
@bot.command(pass_context = True)
async def test(ctx, member : discord.Member):
    row = ActionRow(
            Button(
                style=ButtonStyle.gray,
                label='🔑',  # Эмодзи/Слово (Кнопка)
                custom_id='verif_button'))
    await ctx.send(content="wdwd", components=[row])
#----------------------------------------------------------------



async def clear_message(ctx,count = 1):
    await ctx.channel.purge(limit = int(count))

bot.run(config.xoch, bot = False)