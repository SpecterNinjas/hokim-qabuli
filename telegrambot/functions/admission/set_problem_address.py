from telegram import Bot, Update
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang, send_saved_message_text, save_data_to_cache


@log_errors
def set_problem_address(bot: Bot, update: Update):
    print('set_problem_address')
    user = get_user_lang(update.effective_chat.id)
    try:
        save_data_to_cache(external_id=update.effective_chat.id, data=update.message.location,
                           request_name='problem_address')
    except:
        location = update.message.text
        save_data_to_cache(external_id=update.effective_chat.id, data=location,
                           request_name='problem_address')
    send_saved_message_text(user, bot, update)

