from django.core.cache import cache
from telegram import Bot, Update
from telegrambot import functions
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang, saved_message_text


@log_errors
def set_phone_number(bot: Bot, update: Update):
    print('set_phone_number')

    user = get_user_lang(update.effective_chat.id)

    phone_number = update.message.contact.phone_number

    request = cache.get(f'request_{update.effective_chat.id}')
    request['phone_number'] = phone_number
    cache.set(f'request_{update.effective_chat.id}', request)

    text = saved_message_text(user)

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )
    return functions.main_menu(bot, update)
