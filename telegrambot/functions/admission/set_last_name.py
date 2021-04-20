import re

from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update

from telegrambot import states, functions
from telegrambot.apps import log_errors


@log_errors
def set_last_name(bot: Bot, update: Update):
    print('set_last_name')
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    last_name = update.message.text

    if re.search(r"[0-9]", last_name):
        if user.lang == 'ru':
            err_text = 'Неправильный формат фамилии. Попробуйте еще раз.'
        else:
            err_text = "📝 *Iltimos, familyangizni kiriting:*\n\n" \
                       "❗️_Iltimos, familyangizni kiritishda harflardan foydalaning._"
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=err_text,
            parse_mode='Markdown'
        )
        return states.GET_LAST_NAME

    request = cache.get(f'request_{update.effective_chat.id}')
    request['last_name'] = last_name
    cache.set(f'request_{update.effective_chat.id}', request)

    if user.lang == 'uz':
        text = 'Saqlandi'
    else:
        text = 'Сохранено'

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )

    return functions.admission.get_middle_name(bot, update)
