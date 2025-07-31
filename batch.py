from pyrogram import Client, filters

@Client.on_message(filters.command("batch") & filters.private)
async def batch_handler(client, message):
    await message.reply("📦 Send me the list of files (one per line). Type `done` when finished.")
    batch_list = []

    async for user_msg in client.listen(message.chat.id):
        if user_msg.text.lower() == "done":
            break
        batch_list.append(user_msg.text)

    await message.reply(f"✅ Batch of {len(batch_list)} files received!")
    # TODO: Send all files or links from batch_list
