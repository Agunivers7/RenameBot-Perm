import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5694266322:AAFuhovA-kFby3QNJjTlGUttDxWtYUNdYuA")

    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 10651048))
    API_HASH = os.environ.get("API_HASH","37775aca7d11f450ecde375baac17fe7")
    # Get these values from my.telegram.org

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Aadhi:42426840@cluster0.jqzpafx.mongodb.net/?retryWrites=true&w=majority")

