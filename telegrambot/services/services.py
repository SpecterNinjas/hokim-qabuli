from django.apps import apps
from django.core.cache import cache
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


def save_data_to_cache(external_id, data, request_name):
    request = cache.get(f'request_{external_id}')
    request[f'{request_name}'] = data
    cache.set(f'request_{external_id}', request)
