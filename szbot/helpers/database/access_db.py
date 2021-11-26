import os
from config import MONGODB_URI, BOT_USERNAME
from szbot.helpers.database.database import Database

db = Database(MONGODB_URI, BOT_USERNAME)
