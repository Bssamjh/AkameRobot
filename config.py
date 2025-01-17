from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", "25132383"))
    API_HASH = getenv("API_HASH", "78f258fcc057113beec90a803715425a")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    STRING_SESSION = getenv("STRING_SESSION", None)
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "6244155983:AAFgcD9NpazGQRNGmx68z046GoRcXnlqs2k")
    OWNER_ID = int(getenv("OWNER_ID", "5860129883"))  # sᴛᴀʀᴛ @Akame_Robot ᴛʏᴘᴇ /id
    OWNER_USERNAME = getenv("OWNER_USERNAME", "cxzresa")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "tsaewzmn")
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
    MONGO_URI = getenv("MONGO_DB_URI")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL")

    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
