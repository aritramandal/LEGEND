# Plugin Made BY @Anonymous_Machinee 
# Use With Or Without Credit
# Originally Made for Phantom Userbot
# HAPPY DIWALI TO ALL
# Now to be used in LEGEND USERBOT

from telethon import events
import asyncio 
from Userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="diwali"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 24)
    animation_chars = [          
              "❤️ **Happy Diwali** ❤️",
              "💚 **Happy Diwali** 💚",
              "💜 **Happy Diwali** 💜",
              "💖 **Happy Diwali** 💖",
              "💙 **Happy Diwali** 💙",
              "💛 **Happy Diwali** 💛",
              "💗 **Happy Diwali** 💗",
              "💓 **Happy Diwali** 💓",
              "❤️ **Happy Diwali** ❤️",
              "💚 **Happy Diwali** 💚",
              "💜 **Happy Diwali** 💜",
              "💖 **Happy Diwali** 💖",
              "💙 **Happy Diwali** 💙",
              "💛 **Happy Diwali** 💛",
              "💗 **Happy Diwali** 💗",
              "💓 **Happy Diwali** 💓",
              "❤️ **Happy Diwali** ❤️",
              "💚 **Happy Diwali** 💚",
              "💜 **Happy Diwali** 💜",
              "💖 **Happy Diwali** 💖",
              "💙 **Happy Diwali** 💙",
              "💛 **Happy Diwali** 💛",
              "💗 **Happy Diwali** 💗",
              "💓 **Happy Diwali** 💓",
          ]
    for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %24 ])
    await event.edit("💥 **Happy Diwali** 💥")
    await asyncio.sleep(2)
    await event.edit("🪔 **Happy Diwali to You** 🪔")
            
