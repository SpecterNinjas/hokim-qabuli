from telegram import Bot, Update

from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import save_data_to_cache, send_saved_message_text, get_user_lang


@log_errors
def set_problem_address(bot: Bot, update: Update):
    print('set_problem_address')
    user = get_user_lang(update)

    try:
        location = update.message.location
    except:
        location = update.message.text

    save_data_to_cache(update, location, request_name='location')
    send_saved_message_text(user, bot, update)
    return admission.get_media(bot, update)
