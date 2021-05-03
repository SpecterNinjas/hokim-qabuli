from django.core.cache import cache
from telegram import Bot, Update
from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import get_user_lang, send_saved_message_text, save_data_to_cache, \
    delete_previous_message_with_button


@log_errors
def set_gender(bot: Bot, update: Update):
    print('set_gender')
    user = get_user_lang(update)
    if update.callback_query.data == 'back_to_admission_menu':
        functions.request_menu(bot, update)
        return states.MAIN

    # delete_previous_message_with_button(bot, update)
    save_data_to_cache(update, data=update.callback_query.data, request_name='gender')
    send_saved_message_text(user, bot, update)

    request = cache.get(f'request_{update.effective_chat.id}')
    if request['request_type'] == 'appeal':
        return admission.get_problem_type(bot, update)
    else:
        return admission.get_district(bot, update)
