import re
from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update
from telegrambot import states, functions
from telegrambot.apps import log_errors


@log_errors
def set_middle_name(bot: Bot, update: Update):
    print('set_middle_name')
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)
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
    try:
        bot.delete_message(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id
        )
    except Exception as e:
        print(e)

    request = cache.get(f'request_{update.effective_chat.id}')
    request['middle_name'] = middle_name
    cache.set(f'request_{update.effective_chat.id}', request)

    return functions.admission.get_district(bot, update)
