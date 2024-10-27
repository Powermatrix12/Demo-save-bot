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
    
    # Implement the actual broadcasting logic here (this might vary based on your bot's implementation)
    # You might need a method to broadcast the message to all users, depending on your setup.
    
    await message.reply("Broadcast completed.")

@Bot.on_message(filters.command("stats") & filters.user([OWNER_ID, ADMIN_ID]))
async def stats(client, message):
    # Assuming you have a method to count users; adjust if necessary
    user_count = await client.get_user_count()  # Adjust this based on how you track users
    await message.reply(f"Total users: {user_count}")

@Bot.on_message(filters.command("users") & filters.user([OWNER_ID, ADMIN_ID]))
async def list_users(client, message):
    chat_id = message.chat.id  # Get the chat ID from the message
    members = await client.get_chat_members(chat_id)  # Get members of the chat
    user_list = "\n".join([f"User ID: {member.user.id}, Name: {member.user.first_name}" for member in members])
    
    await message.reply(f"User List:\n{user_list}")

