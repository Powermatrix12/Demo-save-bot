from pymongo import MongoClient
from config import DB_URI

mongo_client = MongoClient(DB_URI)
sessions_collection = mongo_client.userdb.sessions  # Collection for user sessions
premium_users_collection = mongo_client.userdb.premium_users  # Collection for premium users
