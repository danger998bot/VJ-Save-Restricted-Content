import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "16439444"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "98cc0614996ec24abefbdeb3d0fbaea1")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7054450549"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sibasahu036:U2SRRz3W1Q7lZLwK@cluster0.7qoey.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
