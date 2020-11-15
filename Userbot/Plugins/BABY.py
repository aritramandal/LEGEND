# This plugin made by noob @none1p.. don't copy it plzz.. credit goes to @none1p
from telethon import events
import asyncio
import os
import sys
from userbot.utils import admin_cmd
import random

img1=("https://telegra.ph/file/2479b98d08eed6308dfba.mp4")
img2=("https://telegra.ph/file/f81f5ecbcb5ad7c07c093.mp4")
img3=("https://telegra.ph/file/a8feefcdfc6adcda499bf.mp4")
img4=("https://telegra.ph/file/c9b14ac778ffbae2b8877.mp4")
img5=("https://telegra.ph/file/4be0c8224a6b49b796505.mp4")
img6=("https://telegra.ph/file/ee2bb9d5c4c41751c0cd1.mp4")
img7=("https://telegra.ph/file/e982bd34bc29b2908a218.mp4")
img8=("https://telegra.ph/file/f7b2555d6e5c11cd94d8f.mp4")
img9=("https://telegra.ph/file/30df9bd45b861fd0f5773.mp4")
img10=("https://telegra.ph/file/f5364c94795991747f9a7.mp4")
img11=("https://telegra.ph/file/227dc0c3315061e25a5b4.mp4")
img12=("https://telegra.ph/file/c3f47d45cf14ceb0c70f4.mp4")
img13=("https://telegra.ph/file/3d3e86283953a292aef4a.mp4")
img14=("https://telegra.ph/file/6311a00f207a1702183e2.mp4")
img15=("https://telegra.ph/file/6a561f28fa2e3151e19ce.mp4")
img16=("https://telegra.ph/file/2e6647c61f188addc10d6.mp4")
    
    
@borg.on(admin_cmd(outgoing=True, pattern="baby"))

async def _(event):

    if event.fwd_from:
        return
    await event.edit("SENDING...:-)")
    await asyncio.sleep(0.9)
    x=(random.randrange(1,16))
    if x==1:
        await borg.send_file(event.chat_id,img1)
        await event.delete()
    if x==2:
        await borg.send_file(event.chat_id,img2)
        await event.delete()
    if x==3:
        await borg.send_file(event.chat_id,img3)
        await event.delete()
    if x==4:
        await borg.send_file(event.chat_id,img3)
        await event.delete()        
    if x==5:
        await borg.send_file(event.chat_id,img4)
        await event.delete()
    if x==6:
        await borg.send_file(event.chat_id,img5)
        await event.delete()
    if x==7:
        await borg.send_file(event.chat_id,img6)
        await event.delete()
    if x==8:
        await borg.send_file(event.chat_id,img7)
        await event.delete()        
    if x==9:
        await borg.send_file(event.chat_id,img9)
        await event.delete()        
    if x==10:
        await borg.send_file(event.chat_id,img10)
        await event.delete()
    if x==11:
        await borg.send_file(event.chat_id,img11)
        await event.delete()
    if x==12:
        await borg.send_file(event.chat_id,img12)
        await event.delete()
    if x==13:
        await borg.send_file(event.chat_id,img13)
        await event.delete()         
    if x==14:
        await borg.send_file(event.chat_id,img14)
        await event.delete()
    if x==15:
        await borg.send_file(event.chat_id,img15)
        await event.delete()
    if x==16.:
        await borg.send_file(event.chat_id,img16)
        await event.delete()
    # don't copy please😭