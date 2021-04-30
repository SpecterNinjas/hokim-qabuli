import re
from django.core.cache import cache
from telegram import Bot, Update

from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang, send_saved_message_text


@log_errors
def set_first_name(bot: Bot, update: Update):
    print('set_first_name')

    user = get_user_lang(update.effective_chat.id)
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
    request['telegram_id'] = update.effective_chat.id
    cache.set(f'request_{update.effective_chat.id}', request)

    send_saved_message_text(user, bot, update)

    return functions.admission.get_last_name(bot, update)
