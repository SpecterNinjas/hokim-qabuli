import re
from django.core.cache import cache
from telegram import Bot, Update
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import send_saved_message_text, get_user_lang, delete_previous_message_with_button


@log_errors
def set_name(bot: Bot, update: Update):
    print('set_name')
    user = get_user_lang(update)

    try:
        callback = update.callback_query.message.reply_markup.inline_keyboard[0][0]
        name = callback.text
    except:
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
    request['name'] = name
    request['telegram_id'] = update.effective_chat.id
    cache.set(f'request_{update.effective_chat.id}', request)

    delete_previous_message_with_button(bot, update, request_name='callback_message_id')
    send_saved_message_text(user, bot, update)

    return admission.get_birth_year(bot, update)
