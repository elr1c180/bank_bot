from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

comm = InlineKeyboardBuilder()
comm.add(
    types.InlineKeyboardButton(
        text="Community",
        url="https://t.me/clickbankcoin"
    )
)