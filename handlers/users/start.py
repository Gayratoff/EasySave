import requests
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from loader import dp, bot
import time

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")



@dp.message_handler(Text(startswith="https://youtube.com/shorts/"))
async def bot_start(message: types.Message):
    try:
        msg = await message.answer("⏳")
        time.sleep(3)
        await msg.delete()
        api = requests.get(f"https://alijonov.tk/alijonov/api.php?url={message.text}").json()
        api_vid = api['url'][0]['url']
        api_title = api['meta']['title']
        user_id = message.from_user.id
        await bot.send_video(chat_id=user_id, video=api_vid,caption=f"{api_title}\n\n@EasySave_bot")
    except:
        await message.answer("Yuklashni iloji bo'lmadi")

@dp.message_handler(Text(startswith="https://youtu.be/"))
async def bot_start(message: types.Message):
    try:
        msg = await message.answer("⏳")
        time.sleep(3)
        await msg.delete()
        api = requests.get(f"https://alijonov.tk/alijonov/api.php?url={message.text}").json()
        api_vid = api['url'][0]['url']
        api_title = api['meta']['title']
        print(api_vid)
        user_id = message.from_user.id
        await bot.send_video(chat_id=user_id, video=api_vid,caption=f"{api_title}\n\n@EasySave_bot")
    except:
        await message.answer("Yuklashni iloji bo'lmadi")



@dp.message_handler(Text(startswith="https://vm.tiktok.com/"))
async def bot_start(message: types.Message):
    try:
        msg = await message.answer("⏳")
        time.sleep(3)
        await msg.delete()
        api = requests.get(f"https://alijonov.tk/alijonov/api.php?url={message.text}").json()
        api_vid = api['url'][0]['url']
        api_title = api['meta']['title']
        user_id = message.from_user.id
        await bot.send_video(chat_id=user_id, video=api_vid,caption=f"{api_title}\n\n@EasySave_bot")
    except:
        await message.answer("Yuklashni iloji bo'lmadi")

@dp.message_handler(Text(startswith="https://www.tiktok.com/"))
async def bot_start(message: types.Message):
    try:
        msg = await message.answer("⏳")
        time.sleep(3)
        await msg.delete()
        api = requests.get(f"https://alijonov.tk/alijonov/api.php?url={message.text}").json()
        api_vid = api['url'][0]['url']
        api_title = api['meta']['title']
        user_id = message.from_user.id
        await bot.send_video(chat_id=user_id, video=api_vid,caption=f"{api_title}\n\n@EasySave_bot")
    except:
        await message.answer("Yuklashni iloji bo'lmadi")
