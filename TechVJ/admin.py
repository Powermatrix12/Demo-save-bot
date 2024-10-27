from pyrogram import Client, filters
from config import OWNER_ID, ADMIN_ID
from main import Bot

@Bot.on_message(filters.command("broadcast") & filters.user([OWNER_ID, ADMIN_ID]))
async def broadcast_message(client, message):
    if len(message.command) < 2:
        await message.reply("Usage: /broadcast <message>")
        return

    broadcast_text = " ".join(message.command[1:])
    await message.reply("Broadcasting message...")
    await client.broadcast(broadcast_text)
    await message.reply("Broadcast completed.")

@Bot.on_message(filters.command("stats") & filters.user([OWNER_ID, ADMIN_ID]))
async def stats(client, message):
    user_count = await client.get_user_count()
    await message.reply(f"Total users: {user_count}")

@Bot.on_message(filters.command("users") & filters.user([OWNER_ID, ADMIN_ID]))
async def list_users(client, message):
    users = await client.get_all_users()
    user_list = "\n".join([f"User ID: {user['user_id']}" for user in users])
    await message.reply(f"User List:\n{user_list}")
