from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegrambot import states
from telegrambot.models import Text
from telegrambot.services import get_user_lang


def get_problem_address(bot: Bot, update: Update):
    print('get_problem_address')
    user = get_user_lang(update)

    data = Text.objects.filter(text_id='GET_PROBLEM_ADDRESS').values()[0]
    text = data[user.lang]

    if user.lang == 'ru':
        keyboard = [
            [KeyboardButton('📍Поделиться локацией', request_contact=True)]
        ]
    else:
        keyboard = [
            [KeyboardButton('📍Joylashuv ulashish', request_contact=True)]
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
            parse_mode='Markdown'
        )
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
            parse_mode='Markdown',
        )
    return states.GET_PROBLEM_ADDRESS
