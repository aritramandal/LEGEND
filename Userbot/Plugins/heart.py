#Made By @Kraken_The_BadASS . Keep Credits. Cause It hurts. Join @testpy12 for more.



from telethon import events
import asyncio
from Userbot.utils import admin_cmd
from Userbot import ALIVE_NAME
import random
import re
from Userbot import CMD_HELP
from collections import deque



@borg.on(admin_cmd(pattern=r"aheart$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.3
    animation_ttl = range(0, 54)
    animation_chars = [
            "❤️",
            "🧡",
            "💛",
            "💚",
            "💙",
            "💜",
            "🖤",
            "💘",
            "💝",
            "💖",
            "💗",
            "💓",
            "💞",
            "💕",
            "❣️",
            "💔",
            "❤️",
            "🧡",
            "💛",
            "💚",
            "💙",
            "💜",
            "🖤",
            "💘",
            "💝",
            "💖",
            "💗",
            "💓",
            "💞",
            "💕",
            "❣️",
            "💔"
        ]
    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 32])  
            
            
