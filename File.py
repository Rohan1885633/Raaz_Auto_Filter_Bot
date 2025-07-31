from pyrogram import Client, filters

@Client.on_message(filters.command("file") & filters.private)
async def file_handler(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: `/file filename`", quote=True)
    filename = message.text.split(" ", 1)[1]
    await message.reply(f"🔍 Searching for file: `{filename}`...")
    # TODO: Add logic to search file in database and send
