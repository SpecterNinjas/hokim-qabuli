import re
from django.core.cache import cache
from telegram import Bot, Update
from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang, saved_message_text


@log_errors
def set_middle_name(bot: Bot, update: Update):
    print('set_middle_name')

    user = get_user_lang(update.effective_chat.id)

    middle_name = update.message.text

    if re.search(r"[0-9]", middle_name):
        if user.lang == 'ru':
            err_text = 'Неправильный формат отчества. Попробуйте еще раз.'
        else:
            err_text = "📝 *Iltimos, sharfingizni kiriting:*\n\n" \
                       "❗️_Iltimos, sharfingizni kiritishda harflardan foydalaning._"
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=err_text,
            parse_mode='Markdown'
        )
        return states.GET_MIDDLE_NAME

    request = cache.get(f'request_{update.effective_chat.id}')
    request['middle_name'] = middle_name
    cache.set(f'request_{update.effective_chat.id}', request)

    text = saved_message_text(user)

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )

    return functions.admission.get_district(bot, update)
