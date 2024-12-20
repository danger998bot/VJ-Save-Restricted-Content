import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22336285"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3d84051d72e78013f6b38a1b7e26e469")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7547798233"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sibasahu036:f28evZw6b5K0JfeK@cluster0.7qoey.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
