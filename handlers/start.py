from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from kb.start import comm
from function import create_user, new_referal
import asyncio

CLICK_BANK_STICKER = 'CAACAgIAAxkBAAEHkP1mtcSA0ItRC1SbC3ucl32VWuz2zAACX2AAAoFAqUngjH93AAGobFw1BA'

router = Router() 

@router.message(Command("start"))  
async def cmd_start(message: Message):

    command = message.text
    parts = command.split()
    
    if len(parts) > 1:
        start_param = parts[1]
        
        # await message.reply(f"Вы передали параметр: {start_param}")
        chat_id = message.from_user.id
        username = message.from_user.username
        name = message.from_user.first_name
        link_owner = start_param

        await new_referal.new_ref(chat_id, username, name, link_owner)
    else:
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
