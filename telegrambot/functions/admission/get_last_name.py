from telegram import Bot, Update
from telegrambot.services import get_user_lang, edit_or_send_message
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text


@log_errors
def get_last_name(bot: Bot, update: Update):
    print('get_last_name')

    user = get_user_lang(update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_LAST_NAME').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    edit_or_send_message(bot, update, text, inline_keyboard)
    return states.GET_LAST_NAME
