import discord
import random
import requests
import sqlite3
import datetime
import re
import asyncio
import urllib
from discord import member
from discord.ext import commands
from discord.utils import get
 
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime, date, time
from discord.ext import commands
 
import sqlite3
import os
from yt_dlp import YoutubeDL

global ffmpeg_options, flash_bot_time, green_list, ydl_opts
green_list=[852442426542260274]
flash_bot_time = 0
ffmpeg_options = {
    'options': '-vn'}
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec':'mp3',
        'preferredquality': '192'
    }
    ]
}


PATH =r"C:\Users\Xochi\OneDrive\Documents\testbot"

class Selfbot:
    def __init__(self):
        pass

    async def vcconnect(self,ctx,member):
        bot_voice = get(self.bot.voice_clients,guild = ctx.guild_id)

        if bot_voice == None:
            try:
                await member.voice.channel.connect()
            except:
                guild = await self.bot.fetch_guild(ctx.guild_id)
                voice = get(self.bot.voice_clients, guild = guild)
                await voice.disconnect()
                await member.voice.channel.connect()
        
                
    async def play_music(self,ctx):
        try:
            path = PATH + '\song.mp3'
            guild = await self.bot.fetch_guild(ctx.guild_id)
            voice =get(self.bot.voice_clients, guild = guild)
            print(voice)
            voice.play(discord.FFmpegPCMAudio(path,**ffmpeg_options))
       
        except:
            voice.stop()
            voice =get(self.bot.voice_clients,guild = ctx.guild_id)
            voice.play(discord.FFmpegPCMAudio(path,**ffmpeg_options))
            
    async def downdload_music(self,url):
        
        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                os.remove(file)
        
        with YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url[0]])
            except:
                text=''
                for i in url:
                    text+=i+'+'
                html = requests.get(f'https://www.youtube.com/results?search_query={text}')
                video_ids = re.findall(r'watch\?v=(\S{11})', html.text)
                ydl.download([f'https://www.youtube.com/watch?v={video_ids[0]}'])
            for file in os.listdir('./'):
                if file.endswith('.mp3'):
                    os.rename(file, 'song.mp3')

class Main( Selfbot):
    def __init__(self,bot):
        self.bot = bot
