# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, ADMIN_ID
from database.db import sessions_collection, premium_users_collection

class Bot(Client):

    def __init__(self):
        super().__init__(
            "techvj login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="TechVJ"),
            workers=50,
            sleep_threshold=10
        )

    async def start(self):
        await super().start()
        print('Bot Started Powered By @VJ_Botz')

    async def stop(self, *args):
        await super().stop()
        print('Bot Stopped Bye')

    async def check_usage(self, user_id):
        user_data = await sessions_collection.find_one({"user_id": user_id})
        is_premium = await premium_users_collection.find_one({"user_id": user_id})

        if is_premium:
            return 50  # Premium users get 50 uses
        else:
            return 5   # Free users get 5 uses

    async def broadcast(self, message):
        async for user in sessions_collection.find():
            try:
                await self.send_message(user["user_id"], message)
            except Exception as e:
                print(f"Failed to send message to {user['user_id']}: {e}")

    async def get_user_count(self):
        return await sessions_collection.count_documents({})
