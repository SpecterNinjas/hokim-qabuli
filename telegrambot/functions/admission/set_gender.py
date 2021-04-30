from telegram import Bot, Update

from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.models import Text
from telegrambot.services import get_user_lang, send_saved_message_text
from telegrambot.services.services import save_data_to_cache


@log_errors
def set_gender(bot: Bot, update: Update):
    print('set_gender')
    callback_data = update.callback_query.data

    user = get_user_lang(update.effective_chat.id)
    data = Text.objects.filter(text_id='GET_GENDER').values()[0]

    button_texts = data[f"buttons_{user.lang}"].splitlines()
    for button_text in button_texts:
        buttons = button_text.split('|')
        for button in buttons:
            if callback_data == button.split('>')[1]:
                gender = button.split('>')[0]
    if callback_data == 'back_to_admission_menu':
        functions.main_menu(bot, update)
        return states.MAIN
    save_data_to_cache(external_id=update.effective_chat.id, data=gender, request_name='gender')
    send_saved_message_text(user, bot, update)

    return admission.get_district(bot, update)
