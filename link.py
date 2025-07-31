from pyrogram import Client, filters

@Client.on_message(filters.command("link") & filters.private)
async def link_handler(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: `/link filename`", quote=True)
    filename = message.text.split(" ", 1)[1]
    await message.reply(f"🔗 Generating link for: `{filename}`...")
    # TODO: Generate and send direct link
