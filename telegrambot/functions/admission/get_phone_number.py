from telegram import Bot, Update, KeyboardButton
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.models import Text
from telegrambot.services import get_user_lang
from telegrambot.services.services import delete_or_send_message


@log_errors
def get_phone_number(bot: Bot, update: Update):
    print('get_phone_number')

    user = get_user_lang(update)
    data = Text.objects.filter(text_id='GET_PHONE_NUMBER').values()[0]

    if user.lang == 'ru':
        keyboard = [
            [KeyboardButton('☎Поделиться номером', request_contact=True)]
        ]
    else:
        keyboard = [
            [KeyboardButton('☎Raqamni ulashish', request_contact=True)]
        ]
    delete_or_send_message(bot, update, keyboard, text=data[user.lang])
    return states.GET_PHONE_NUMBER
