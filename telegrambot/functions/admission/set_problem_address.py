from django.core.cache import cache
from telegram import Bot, Update
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import get_user_lang, send_saved_message_text, save_data_to_cache


@log_errors
def set_problem_address(bot: Bot, update: Update):
    print('set_problem_address')
    user = get_user_lang(update.effective_chat.id)

    if update.message.location is None:
        problem_address = update.message.text
        save_data_to_cache(external_id=update.effective_chat.id, data=problem_address,
                           request_name='problem_address')
    else:
        save_data_to_cache(external_id=update.effective_chat.id, data=update.message.location,
                           request_name='problem_address')

    send_saved_message_text(user, bot, update)
    return admission.get_media(bot, update)
