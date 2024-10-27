import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7944698234:AAEQYS5I8Cg1jw7YrKgOnbGB5XGJlIUX_zI")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26258063"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "be0a0e2ecd938bfc5401d35a399deeb7")

# Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://katay57920:wz3U1N6lG8DKsDBx@clusterex.npb0e.mongodb.net/?retryWrites=true&w=majority")

# Owner and Admin IDs
OWNER_ID = int(os.environ.get("OWNER_ID", "6706434927"))  # Replace with your actual owner ID
ADMIN_ID = int(os.environ.get("ADMIN_ID", "5904478052"))  # Replace with your actual admin ID
