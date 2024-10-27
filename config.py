import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "YOUR_API_ID"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "YOUR_API_HASH")

# Database 
DB_URI = os.environ.get("DB_URI", "YOUR_DB_URI")

# Owner and Admin IDs
OWNER_ID = int(os.environ.get("OWNER_ID", "YOUR_OWNER_ID"))  # Replace with your actual owner ID
ADMIN_ID = int(os.environ.get("ADMIN_ID", "YOUR_ADMIN_ID"))  # Replace with your actual admin ID
