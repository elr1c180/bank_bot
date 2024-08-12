from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from kb.start import comm
from function import create_user
import asyncio

CLICK_BANK_STICKER = 'CAACAgIAAxkBAAEHkP1mtcSA0ItRC1SbC3ucl32VWuz2zAACX2AAAoFAqUngjH93AAGobFw1BA'

router = Router() 

@router.message(Command("start"))  
async def cmd_start(message: Message):

    chat_id = message.from_user.id
    username = message.from_user.username
    name = message.from_user.first_name
    

    await create_user.create_user(chat_id, username, name)

    await message.answer_sticker(CLICK_BANK_STICKER)
    await message.answer(
        "Welcome!\nStart your new life with <b>Click Bank</b>",
        reply_markup=comm.as_markup(),
        parse_mode='html'
        )
