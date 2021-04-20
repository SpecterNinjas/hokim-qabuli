from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update, ReplyKeyboardRemove


def set_short_description(bot: Bot, update: Update):
    print('set_short_description')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    short_description = update.message.text

    request = cache.get(f'request_{update.effective_chat.id}')
    request['short_description'] = short_description
    cache.set(f'request_{update.effective_chat.id}', request)

    if user.lang == 'uz':
        text = 'Saqlandi'
    else:
        text = 'Сохранено'

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )
