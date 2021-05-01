from telegram import Update, Bot
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang, edit_or_send_message


@log_errors
def get_birth_day(bot: Bot, update: Update):
    print('get_birth_day')
    user = get_user_lang(update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_BIRTH_DAY').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    edit_or_send_message(bot, update, text, inline_keyboard)
    return states.GET_BIRTH_DAY
