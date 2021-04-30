from telegram import Bot, Update
from telegrambot import functions
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang, saved_message_text
from telegrambot.services.services import save_data_to_cache


@log_errors
def set_phone_number(bot: Bot, update: Update):
    print('set_phone_number')

    user = get_user_lang(update.effective_chat.id)

    save_data_to_cache(external_id=update.effective_chat.id, data=update.message.contact.phone_number,
                       request_name='phone_number')

    text = saved_message_text(user)

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )
    return functions.main_menu(bot, update)
