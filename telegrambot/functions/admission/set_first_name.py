import re

from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update

from telegrambot import states, functions
from telegrambot.apps import log_errors


@log_errors
def set_first_name(bot: Bot, update: Update):
    print('set_first_name')
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)
    name = update.message.text

    if re.search(r"[0-9]", name):
        if user.lang == 'ru':
            err_text = 'Неправильный формат имени. Попробуйте еще раз.'
        else:
            err_text = "📝 *Iltimos, ismingizni kiriting:*\n\n" \
                       "❗️_Iltimos, ismingizni kiritishda harflardan foydalaning._"
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=err_text,
            parse_mode='Markdown'
        )

        return states.GET_FIRST_NAME

    request = cache.get(f'request_{update.effective_chat.id}')
    request['first_name'] = name
    cache.set(f'request_{update.effective_chat.id}', request)

    return functions.admission.get_last_name(bot, update, data=None, edit=False)
