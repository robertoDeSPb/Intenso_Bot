import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy import create_engine, text

engine = create_engine(config("PG_LINK"))
with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS IntensoBot"))
    conn.commit()

engine = create_engine(config("PG_LINK") + "/IntensoBot", echo=False, future=True)

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]

logging.basicConfig(level=logging.INFO, format ='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
#user_prev_menu = {}
bot = Bot(token=config('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
