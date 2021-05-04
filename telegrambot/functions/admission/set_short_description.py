from django.core.cache import cache
from telegram import Bot, Update
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import send_saved_message_text, save_data_to_cache, get_user_lang, \
    delete_previous_message_with_button


@log_errors
def set_short_description(bot: Bot, update: Update):
    print('set_short_description')
    save_data_to_cache(update, update.message.text, request_name='short_description')
    send_saved_message_text(get_user_lang(update), bot, update)
    delete_previous_message_with_button(bot, update, request_name='callback_message_id')
    request = cache.get(f'request_{update.effective_chat.id}')
    if request['request_type'] == 'appeal':
        return admission.get_problem_address(bot, update)
    else:
        return admission.get_phone_number(bot, update)
