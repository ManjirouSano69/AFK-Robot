from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("API_ID", "22867431"))
API_HASH = getenv("API_HASH", "24ef0e76ceb137563dc33722e4cd79bd")

BOT_TOKEN = getenv("BOT_TOKEN", "7340557811:AAH5AkYPuilpuPHz0hJjDGtnT9PQ9W2U_w4")
LOG_ID = int(getenv("LOG_ID", "-1002197525160"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://niksharma92297:afk@cluster0.wj4ftow.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SUDO_USER = list(map(int, getenv("SUDO_USER", "1993048420 5743248220").split()))
