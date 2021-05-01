from telegram import Bot, Update
from telegrambot import states
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang, edit_or_send_message


def get_social_security_problem(bot: Bot, update: Update):
    print('get_social_security_problem')

    user = get_user_lang(update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_SOCIAL_SECURITY_PROBLEM').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    edit_or_send_message(bot, update, text, inline_keyboard)
    return states.GET_SOCIAL_SECURITY_PROBLEM
