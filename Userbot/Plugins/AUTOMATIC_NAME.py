"""Auto Profile Updation Commands
.autoname"""
from telethon import events
import asyncio
import time
from telethon.tl import functions
from telethon.errors import FloodWaitError
from uniborg.util import admin_cmd
from Userbot import ALIVE_NAME


DEL_TIME_OUT = 10
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𖤍𖤍𖤍☞𝕃𝔼𝔾𝔼ℕ𝔻 𝕌𝔹☜𖤍𖤍𖤍"


@borg.on(admin_cmd(pattern="aname"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        name = f"⏱{HM}⏱ 💎{DEFAULTUSER}💎 🗓{DMY}🗓"
        logger.info(name)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=name
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
    
        # else:
            # logger.info(r.stringify())
            # await borg.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Name"
            # )
        await asyncio.sleep(DEL_TIME_OUT)
    await event.edit(f"Auto Name has been started .. please check your profile 📷") 
