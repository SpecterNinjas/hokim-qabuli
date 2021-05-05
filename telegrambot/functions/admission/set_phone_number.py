from telegrambot import functions
from telegram import Bot, Update
from telegrambot.apps import log_errors
from telegrambot.services import send_saved_message_text, get_user_lang, save_data_to_cache


@log_errors
def set_phone_number(bot: Bot, update: Update):
    print('set_phone_number')
    user = get_user_lang(update)

    phone_number = update.message.contact.phone_number

    save_data_to_cache(update, phone_number, request_name='phone_number')

    send_saved_message_text(user, bot, update)

    return functions.request_menu(bot, update)
