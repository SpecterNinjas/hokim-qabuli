from telegram import Bot, Update
from telegrambot.functions import admission
from telegrambot.services import send_saved_message_text, save_data_to_cache, get_user_lang


def set_short_description(bot: Bot, update: Update):
    print('set_short_description')

    user = get_user_lang(update)
    save_data_to_cache(update, update.message.text, request_name='short_description')
    send_saved_message_text(user, bot, update)

    return admission.get_phone_number(bot, update)
