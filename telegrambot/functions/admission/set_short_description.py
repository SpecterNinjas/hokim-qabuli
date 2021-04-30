from django.core.cache import cache
from telegram import Bot, Update, ReplyKeyboardRemove
from telegrambot.functions import admission
from telegrambot.services import get_user_lang, saved_message_text
from telegrambot.services.services import save_data_to_cache


def set_short_description(bot: Bot, update: Update):
    print('set_short_description')

    user = get_user_lang(update.effective_chat.id)

    short_description = update.message.text

    request = cache.get(f'request_{update.effective_chat.id}')
    save_data_to_cache(external_id=update.effective_chat.id, data=short_description, request_name='short_description')

    text = saved_message_text(user)

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )
    if request['request_type'] == 'appeal':
        return admission.get_file(bot, update)
    else:
        return admission.get_phone_number(bot, update)
