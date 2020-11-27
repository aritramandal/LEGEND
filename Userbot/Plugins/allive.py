import asyncio
from telethon import events
from userbot.utils import admin_cmd
from . import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND USERBOT"

PM_IMG = "https://telegra.ph/file/fd4b1081e8e297dc4a701.jpg"

pm_caption = " LEGEND USERBOT is working successfully \n\n"

pm_caption += f" **••Mу Bσѕѕ••**     :   {DEFAULTUSER}\n"

pm_caption += " **тєℓєтнσи νєяѕισи** :   1.15.0 \n"

pm_caption += " **σffι¢ιαℓ ¢нαииєℓ** :   [ᴊᴏɪɴ](https://t.me/LEGEND_USERBOT_SUPPORT)\n"

pm_caption += " σffι¢ιαℓ gяσυρ       :   [ᴊᴏɪɴ](https://t.me/Eliza_userbot_group)\n"

pm_caption += " ℓι¢єиѕє              :   [ӀíϲҽղՏҽ](https://github.com/aritramandal/LEGEND/blob/master/LICENSE)\n"

#@command(outgoing=True, pattern="^.allive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 

