from telegram import Bot, Update, KeyboardButton
from telegrambot import states
from telegrambot.models import Text
from telegrambot.services import get_user_lang
from telegrambot.services.services import delete_or_send_message


def get_problem_address(bot: Bot, update: Update):
    print('get_problem_address')
    user = get_user_lang(update)

    data = Text.objects.filter(text_id='GET_PROBLEM_ADDRESS').values()[0]
    text = data[user.lang]

    if user.lang == 'ru':
        keyboard = [
            [KeyboardButton('📍Поделиться локацией', request_location=True)]
        ]
    else:
        keyboard = [
            [KeyboardButton('📍Joylashuv ulashish', request_location=True)]
        ]

    delete_or_send_message(bot, update, keyboard, text)
    return states.GET_PROBLEM_ADDRESS
