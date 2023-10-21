#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6786994011:AAGVbaxRtScxXu2KNMsN1-JuuPTtxOisk8Q")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22418774"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d8c8dab274f9a811814a6a96d044028e")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002018301849"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5493260414"))

#Port
PORT = os.environ.get("PORT", "8040")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://mehtadmphta33:Mehtab1234@cluster0.80db0ve.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001800113147"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001923816775"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>𝗛𝗲𝘆 {first}🖐️ 🥲\n\n𝗜 𝗮𝗺 𝗮𝗻 𝗮 𝗳𝗶𝗹𝗲 𝘀𝘁𝗼𝗿𝗲 𝗯𝗼𝘁 𝗯𝗮𝘀𝗶𝗰𝗮𝗹𝗹𝘆 𝗳𝗼𝗿 @Anime_Chidori</b>.")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "6376328008").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Sorry Dude You're Not Joined My Channel 😐</b>\n\n<b>So Please Join Our Update Channel To Continue Watching Your Favourite Animes ⚡</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please Avoid Direct Messages. I'm Here merely for file sharing!"

ADMINS.append(OWNER_ID)
ADMINS.append(6376328008)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
