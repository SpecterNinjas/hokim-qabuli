import re

from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update

from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import send_saved_message_text


@log_errors
def set_name(bot: Bot, update: Update):
    print('set_name')
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

        return states.GET_NAME

    request = cache.get(f'request_{update.effective_chat.id}')
    request['first_name'] = name
    request['telegram_id'] = update.effective_chat.id
    cache.set(f'request_{update.effective_chat.id}', request)

    send_saved_message_text(user, bot, update)

    return admission.get_birth_year(bot, update)
