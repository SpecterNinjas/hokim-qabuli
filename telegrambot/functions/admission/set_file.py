from telegram import Bot, Update
from telegrambot.apps import log_errors


@log_errors
def set_file(bot: Bot, update: Update):
    print('set_file')
