from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from kb.start import comm

CLICK_BANK_STICKER = 'CAACAgIAAxkBAAEHkP1mtcSA0ItRC1SbC3ucl32VWuz2zAACX2AAAoFAqUngjH93AAGobFw1BA'

router = Router() 

@router.message(Command("start"))  
async def cmd_start(message: Message):
    await message.answer_sticker(CLICK_BANK_STICKER)
    await message.answer(
        "Welcome!\nStart your new life with <b>Click Bank</b>",
        reply_markup=comm.as_markup(),
        parse_mode='html'
        )