from telegram import Bot, Update
from telegrambot import states
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang
from telegrambot.services.services import edit_or_send_message


def get_problem_type(bot: Bot, update: Update):
    print('get_problem_type')

    user = get_user_lang(update)

    data = Text.objects.filter(text_id='GET_PROBLEM_TYPE').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    edit_or_send_message(bot, update, inline_keyboard=inline_keyboard, text=text)

    return states.GET_PROBLEM_TYPE
