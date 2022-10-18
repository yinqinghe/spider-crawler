import os
import logging
class Config:
    
    API_ID = int(18492620)
    API_HASH = '85e27071262efb643b2e5ccbde965cfb'
    BOT_TOKEN = "5370462470:AAFCi0wwn_WvVhNCQDlXYpixljEIatBcpks" 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "")
    DATABASE_URI = "jdbc:mysql://localhost:3306"
    DATABASE_NAME = "sun"
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "Forward_Session")
    TO_CHANNEL = int(-1001714003588)
    BOT_USERNAME= "@forward_tome_bot"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
