from telegram import Bot, Update

from telegrambot import functions
from telegrambot.services import get_user_lang, send_saved_message_text


def set_change_language(bot: Bot, update: Update):
    print('set_change_language')
    language = update.message.text
    user = get_user_lang(update)
    if language == 'Русский язык':
        user.lang = 'ru'
    else:
        user.lang = 'uz'
    user.save()
    send_saved_message_text(user, bot, update)
    return functions.profile_settings(bot, update)
