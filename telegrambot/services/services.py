from django.apps import apps
from telegram import Update


def get_user_lang(update: Update):
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)
    return user
