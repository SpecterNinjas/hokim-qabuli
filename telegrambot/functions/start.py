from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import get_request_data


@log_errors
def start(bot: Bot, update: Update):
    print('START')
    if cache.get(f'request_{update.effective_chat.id}') is None:
        request = get_request_data()
        cache.set(f'request_{update.effective_chat.id}', request)
    else:
        request = cache.get(f'request_{update.effective_chat.id}')

    cache.set(f'request_{update.effective_chat.id}', request)

    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 O'zbek tili", callback_data='uz_'),
            InlineKeyboardButton('🇷🇺 Русский язык', callback_data='ru_'),
        ]
    ]
    try:
        bot.edit_message_text(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
            text='*Tilni tanlang* / *Выберите язык*',
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text='*Tilni tanlang* / *Выберите язык*',
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    return states.GET_LANG
