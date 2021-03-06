from telegram import Bot, Update
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.models import Text
from telegrambot.services import send_saved_message_text, save_data_to_cache, get_user_lang


@log_errors
def set_land_issues_problem(bot: Bot, update: Update):
    print('set_land_issues')

    user = get_user_lang(update)

    data = Text.objects.filter(text_id='GET_LAND_ISSUES_PROBLEM').values()[0]
    callback_data = update.callback_query.data

    texts = data[f"buttons_{user.lang}"].splitlines()

    for text in texts:
        buttons = text.split('|')
        for button in buttons:
            if callback_data == button.split('>')[1]:
                sub_problem = button.split('>')[0]

    if callback_data == 'back_to_problem_type':
        return admission.get_problem_type(bot, update)

    save_data_to_cache(update, sub_problem, request_name='sub_problem')
    send_saved_message_text(user, bot, update)
    return admission.get_short_description(bot, update)
