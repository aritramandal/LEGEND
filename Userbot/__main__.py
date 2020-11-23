from Userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from Userbot.utils import load_module
from Userbot import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()
    

import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print("☞♨︎ℕ𝕆𝕎, 𝕃𝔼𝔾𝔼ℕ𝔻 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 𝕀𝕊 𝕃𝔸ℕ𝔻𝔼𝔻 ℙ𝔼𝔸ℂ𝔼𝔽𝕌𝕃𝕃𝕐.. 𝕐𝕆𝕌 𝕊ℍ𝕆𝕌𝕃𝔻 𝕋ℍ𝔸ℕ𝕂 @YOU_ARE_UNDER_ARREST 𝔸ℕ𝔻 @none1p 𝕗𝕠𝕣 𝕥𝕙𝕚𝕤 𝕦𝕟𝕚𝕢𝕦𝕖 𝕦𝕤𝕖𝕣𝕓𝕠𝕥 𝕞𝕒𝕕𝕖 𝕓𝕪 𝕥𝕙𝕖𝕞..♨︎☜")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()


 
