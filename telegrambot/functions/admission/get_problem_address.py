from telegram import Bot, Update, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.models import Text
from telegrambot.services import get_user_lang


@log_errors
def get_problem_address(bot: Bot, update: Update):
    print('get_problem_address')
    user = get_user_lang(update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_PROBLEM_ADDRESS').values()[0]
    text = data[user.lang]

    if user.lang == 'ru':
        location_text = '📍Поделиться локацией'
    else:
        location_text = '📍Joylashuv bilan ulashish'

    keyboard = [[KeyboardButton(location_text, request_location=True, )]]

    try:
        bot.delete_message(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
        )
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        )
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        )
    return states.GET_PROBLEM_ADDRESS
