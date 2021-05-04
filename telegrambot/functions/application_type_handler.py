from django.core.cache import cache
from telegram import Bot, Update
from telegrambot import functions


def application_type_handler(bot: Bot, update: Update):
    print('application_type_handler')
    request_type = update.message.text
    request = cache.get(f'request_{update.effective_chat.id}')
    if request_type == 'Hokim qabuliga yozish' or request_type == 'Письмо к приему Хакима':
        request['request_type'] = 'admission'
    elif request_type == 'Hokimga murojat' or request_type == 'Обращение к Хакиму':
        request['request_type'] = 'appeal'
    cache.set(f'request_{update.effective_chat.id}', request)
    return functions.request_menu(bot, update)
