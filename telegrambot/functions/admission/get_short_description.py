from telegram import Bot, Update
from telegrambot.models import Text
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.services import get_user_lang, edit_or_send_message


@log_errors
def get_short_description(bot: Bot, update: Update):
    print('get_short_description')

    user = get_user_lang(update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_SHORT_DESCRIPTION').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    edit_or_send_message(bot, update, text, inline_keyboard)

    return states.GET_SHORT_DESCRIPTION
