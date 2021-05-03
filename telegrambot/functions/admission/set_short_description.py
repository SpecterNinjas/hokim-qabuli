from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update, ReplyKeyboardRemove

from telegrambot.functions import admission
from telegrambot.services import send_saved_message_text


def set_short_description(bot: Bot, update: Update):
    print('set_short_description')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    short_description = update.message.text

    request = cache.get(f'request_{update.effective_chat.id}')
    request['short_description'] = short_description
    cache.set(f'request_{update.effective_chat.id}', request)

    send_saved_message_text(user, bot, update)

    return admission.get_phone_number(bot, update)
