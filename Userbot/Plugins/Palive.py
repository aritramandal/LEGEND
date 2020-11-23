#alive by @YOU_ARE_UNDER_ARREST

import os
import requests
import time
from PIL import Image
from io import BytesIO
from Userbot import ALIVE_NAME
from Userbot.utils import admin_cmd
from datetime import datetime

ALIVE_PHOTO = os.environ.get("ALIVE_PHOTO" , None)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "This user"

@borg.on(admin_cmd(outgoing=True, pattern="palive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTO:
        pm_caption = "**𝕃𝔼𝔾𝔼ℕ𝔻 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 𝙸𝚂 🅉🄸🄽🄳🄰**\n"
        pm_caption += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
        pm_caption += "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 15.0\n"
        pm_caption += "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.8.5\n"
        pm_caption += "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/legend_userbot_support_channel)\n"
        pm_caption += "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/LEGEND_USERBOT_SUPPORT)\n"
        pm_caption += "𝘓𝘐𝘊𝘌𝘕𝘚𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://aritramandal517.wixsite.com/-site)\n"
        pm_caption += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ @YOU_ARE_UNDER_ARREST ](https://t.me/YOU_ARE_UNDER_ARREST)\n"
        pm_caption += "[╔┓┏╦━╦┓╔┓╔━━╗\n║┗┛║┗╣┃║┃║X X║\n║┏┓║┏╣┗╣┗╣╰╯║\n╚┛┗╩━╩━╩━╩━━╝\n](https://t.me/LEGEND_USERBOT_SUPPORT)"
        chat = await alive.get_chat()
        await palive.delete()
        """ For .palive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALIVE_PIC,caption=pm_caption, link_preview = False)
        await palive.delete()
        return
    req = requests.get("https://telegra.ph/file/41daf87744a82b0065fc6.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(alive.chat_id,"**𝕃𝔼𝔾𝔼ℕ𝔻 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 𝙸𝚂 🅉🄸🄽🄳🄰**\n"
                      f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
                      "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 15.0\n"
                      "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.8.5\n"
                      "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/legend_userbot_support_channel)\n"
                      "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/LEGEND_USERBOT_SUPPORT)\n"
                      "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://aritramandal517.wixsite.com/-site)\n"
                      "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ @YOU_ARE_UNDER_ARREST ](https://t.me/YOU_ARE_UNDER_ARREST)\n"
                                "[╔┓┏╦━╦┓╔┓╔━━╗\n║┗┛║┗╣┃║┃║X X║\n║┏┓║┏╣┗╣┗╣╰╯║\n╚┛┗╩━╩━╩━╩━━╝\n](https://t.me/LEGEND_USERBOT_SUPPORT)" , link_preview = False) 
        await palive.delete()
