""" Its jokes time... 

#special thanks bristi @none1p

#made by aritra

    Command .joke


    By @YOU_ARE_UNDER_ARREST""" 

from telethon import events
import asyncio
import os
import sys
import random
from Userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"joke", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("here a fact about you......")
    await asyncio.sleep(1)
    s=(random.randrange(1,10)) 
    if s==1:
         await event.edit("If you are a girl named Khushi and you cry, \n  people won’t take it seriously\n ..Why? \n Because that would be ‘Khushi ke aansoo’!!")
    if s==2:
        await event.edit("I love it when my Sony smartphone hangs and gives me Problems.. \n Because… \n “Sony de Nakhre sohne lagde menu”")

    if s==3:
        await event.edit("Cricket team k jab sab player out ho jate hain,..to sab machaar bhaag jate hain,\n batao kyu??... \n KYUKI team “AllOut” hain naa... \n L \n O \n L")
    if s==4:
        await event.edit("🤔एक बात समझ नहीं आई,🙄 \n सरकार जो इतने कदम  उठाती हैं \n  ,आखिर में रखती कंहा हैं?? \n ☝🏻😝😂😂😂😂😂😂😂😂😂")
    if s==5:
        await event.edit("One day Om Puri came late for the shooting.. \n Cast and crew said….\n \n \n Omelette aaya!!\n 😀")
    if s==6:
        await event.edit("Om Puri was kidnapped by Taliban... \n Govt launched a mission to save him \n .Bolo uss mission kaa naam kya hoga?? \n Answer: Save Puri!")
    if s==7:
        await event.edit("KID :- Why some of ur hair are white dad…?... \n DAD : – Every time you make me unhappy , one of my hair turns white… \n  KID :- Now understand why grandpa’s hairs are all white… \n Moral :- Don’t be over smart….")
    if s==8:
        await event.edit("Santa: Do You Know English? \n Banta: Yes \n Santa: Ok! Then Tell What Is The Opposite Of Naag Panchami? \n Banta:So Simple Yaar.... \n “Naag Don't Punch Me”")
    if s==9:
        await event.edit("Na train mein, \n na phoolo mein \n ..na rasoi mein \n na rain mein... \n dard milta hai to tere diye hue pain mein…😭!")
    if s==10:
        await event.edit("Ladki: Yeh kya kar rahe ho? \n Ladka: Dahi Jama raha hoon… \n Ladki: Kab tak jamaoge? \n Ladka:Agar tum mil jaao... \n Jamana chhod denge hum!😘🌹")
      
    await joke.delete()
 
