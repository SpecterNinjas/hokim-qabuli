from django.apps import apps
from telegram import Bot, Update
from telegrambot import states
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services.services import edit_or_send_message


def get_social_security_problem(bot: Bot, update: Update):
    print('get_social_security_problem')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_SOCIAL_SECURITY_PROBLEM').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    edit_or_send_message(bot, update, inline_keyboard=inline_keyboard, text=text)

    return states.GET_SOCIAL_SECURITY_PROBLEM
