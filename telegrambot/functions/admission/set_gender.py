from telegram import Bot, Update
from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.functions import admission
# from telegrambot.services import get_user_lang, send_saved_message_text
# from telegrambot.services.services import save_data_to_cache, delete_previous_message_with_button


# @log_errors
# def set_gender(bot: Bot, update: Update):
#     print('set_gender')
#     callback_data = update.callback_query.data
#     user = get_user_lang(update.effective_chat.id)
#
#     if callback_data == 'back_to_admission_menu':
#         functions.main_menu(bot, update)
#         return states.MAIN
#
#     delete_previous_message_with_button(bot, update.effective_chat.id)
#     save_data_to_cache(external_id=update.effective_chat.id, data=callback_data, request_name='gender')
#     send_saved_message_text(user, bot, update)
#
#     return admission.get_district(bot, update)
