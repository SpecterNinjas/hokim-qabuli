from django.core.cache import cache
from telegram import Bot, Update
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.models import Text
from telegrambot.services import send_saved_message_text, get_user_lang, save_data_to_cache


@log_errors
def set_social_security_problem(bot: Bot, update: Update):
    print('set_social_security_problem')

    user = get_user_lang(update)

    data = Text.objects.filter(text_id='GET_SOCIAL_SECURITY_PROBLEM').values()[0]
    callback_data = update.callback_query.data

    texts = data[f"buttons_{user.lang}"].splitlines()
    for text in texts:
        buttons = text.split('|')
        for button in buttons:
            if callback_data == button.split('>')[1]:
                sub_problem = button.split('>')[0]

    if callback_data == 'back_to_problem_type':
        return admission.get_problem_type(bot, update)

    save_data_to_cache(update, data=sub_problem, request_name='sub_problem')
    send_saved_message_text(user, bot, update)
    return admission.get_short_description(bot, update)
