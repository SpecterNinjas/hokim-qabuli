from telegram import Bot, Update
from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.models import Text
from telegrambot.services import get_user_lang, send_saved_message_text, save_data_to_cache, \
    delete_previous_message_with_button


@log_errors
def set_gender(bot: Bot, update: Update):
    print('set_gender')

    user = get_user_lang(update)
    data = Text.objects.filter(text_id='GET_GENDER').values()[0]

    texts = data[f"buttons_{user.lang}"].splitlines()
    for text in texts:
        buttons = text.split('|')
        for button in buttons:
            if update.callback_query.data == button.split('>')[1]:
                gender = button.split('>')[0]

    if update.callback_query.data == 'back_to_admission_menu':
        functions.main_menu(bot, update)
        return states.MAIN

    # delete_previous_message_with_button(bot, update)
    save_data_to_cache(update, data=gender, request_name='gender')
    send_saved_message_text(user, bot, update)

    return admission.get_district(bot, update)
