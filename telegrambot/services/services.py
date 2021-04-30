from django.apps import apps
from telegram import Update, Bot


def get_user_lang(external_id):
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=external_id)
    return user


def saved_message_text(user: get_user_lang):
    if user.lang == 'uz':
        text = 'Saqlandi'
    else:
        text = 'Сохранено'

    return text
