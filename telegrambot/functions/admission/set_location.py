from telegram import Bot, Update, InlineKeyboardMarkup

from telegrambot import states
from telegrambot.apps import log_errors


@log_errors
def set_location(bot: Bot, update: Update):
    print('set_location')
