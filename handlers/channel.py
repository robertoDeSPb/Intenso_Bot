from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import create_bot
from create_bot import bot
import os
from db_handler.json_management import add_credentials
from all_media.links import all_media_dir
channel_router = Router()

@channel_router.channel_post()
async def handle_channel_post(message: Message):
    print ("New message")
    if message.document:
        doc = message.document
        print(f"Recieved new file from channel: {doc.file_name} file_id=({doc.file_id})")
        library_dict = {}
        library_dict[doc.file_name] = message.message_id
        add_credentials(library_dict, filename=os.path.join(all_media_dir, "libraries.json"))
