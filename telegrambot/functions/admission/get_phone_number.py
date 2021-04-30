from django.apps import apps
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup

from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.models import Text
from telegrambot.services import get_user_lang


@log_errors
def get_phone_number(bot: Bot, update: Update):
    print('get_phone_number')

    user = get_user_lang(update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_PHONE_NUMBER').values()[0]
    text = data[user.lang]
    if user.lang == 'ru':
        keyboard = [
            [KeyboardButton('☎Поделиться номером', request_contact=True)]
        ]
    else:
        keyboard = [
            [KeyboardButton('☎Raqamni ulashish', request_contact=True)]
        ]

    try:
        bot.delete_message(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
        )
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
            parse_mode='Markdown',
        )
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
            parse_mode='Markdown',
        )
    return states.GET_PHONE_NUMBER