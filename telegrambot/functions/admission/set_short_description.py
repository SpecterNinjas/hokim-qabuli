from django.core.cache import cache
from telegram import Bot, Update
from telegrambot.functions import admission
from telegrambot.services import get_user_lang, send_saved_message_text
from telegrambot.services.services import save_data_to_cache, delete_previous_message_with_button


def set_short_description(bot: Bot, update: Update):
    print('set_short_description')

    user = get_user_lang(update.effective_chat.id)

    short_description = update.message.text

    save_data_to_cache(external_id=update.effective_chat.id, data=short_description, request_name='short_description')
    delete_previous_message_with_button(bot, update.effective_chat.id)
    send_saved_message_text(user, bot, update)

    request = cache.get(f'request_{update.effective_chat.id}')
    if request['request_type'] == 'appeal':
        return admission.get_problem_address(bot, update)
    else:
        return admission.get_phone_number(bot, update)
