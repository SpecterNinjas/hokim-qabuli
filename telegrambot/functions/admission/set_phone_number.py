from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update

from telegrambot import functions


def set_phone_number(bot: Bot, update: Update):
    print('set_phone_number')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    phone_number = update.message.contact.phone_number

    request = cache.get(f'request_{update.effective_chat.id}')
    request['phone_number'] = phone_number
    cache.set(f'request_{update.effective_chat.id}', request)

    if user.lang == 'uz':
        text = 'Saqlandi'
    else:
        text = 'Сохранено'

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )
    return functions.admission_menu(bot, update)
