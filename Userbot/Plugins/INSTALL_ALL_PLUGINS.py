#FOR LEGEND USERBOT By @hellboi_atul...
#Edited by @YOU_ARE_UNDER_ARREST
#INSTALL MANY PLUGINS EK JHATKE ME
from telethon.tl.types import InputMessagesFilterDocument
from Userbot.utils import remove_plugin, load_module, admin_cmd
from Userbot import admin_CMD
import Userbot.utils
import os

@borg.on(admin_cmd(pattern=r"installall$"))
async def install(event):
	if event.fwd_from:
		return
	documentss = await event.client.get_messages(event.chat_id, None ,search='.py', filter=InputMessagesFilterDocument)
	total = int(documentss.total)
	total_doxx = range(0, total)
	b = await event.client.send_message(event.chat_id, f"**Installing {total} plugins...**\n`This msg will be deleted after the installation gets completed`")
	text =  "**Installing...**\n\n"
	a = await event.client.send_message(event.chat_id, text)
	if total == 0:
		await a.edit("**No plugins..what am I supposed to install.**")
		await event.delete()
		return
	for ixo in total_doxx:
		mxo = documentss[ixo].id
		downloaded_file_name = await event.client.download_media(await event.client.get_messages(event.chat_id, ids=mxo), "userbot/plugins/")
		if "(" not in downloaded_file_name:
			path1 = Path(downloaded_file_name)
			shortname = path1.stem
			try:
				load_module(shortname.replace(".py", ""))
				text += f"**• Installed all** `{(os.path.basename(downloaded_file_name))}` **successfully.**\n"
			except:
				text += f"**• Error, can't Install🚶🏻🚶🏻** `{(os.path.basename(downloaded_file_name))}`\n"
		else:
			text += f"**🚀 Plugin** `{(os.path.basename(downloaded_file_name))}` **already installed.**\n"
		await a.edit(f"{text}\n**Installed every plugin from the given chat.**")
		await event.delete()
		await b.delete()
© 2020 GitHub, Inc.
