from django.core.cache import cache
from telegram import Bot, Update
from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.models import Text
from telegrambot.services import get_user_lang
from telegrambot.services.services import save_data_to_cache


@log_errors
def set_problem_type(bot: Bot, update: Update):
    print('set_problem_type')
    
    user = get_user_lang(update.effective_chat.id)

    callback_data = update.callback_query.data
    data = Text.objects.filter(text_id='GET_PROBLEM_TYPE').values()[0]

    texts = data[f"buttons_{user.lang}"].splitlines()
    for text in texts:
        buttons = text.split('|')
        for button in buttons:
            if callback_data == button.split('>')[1]:
                problem_type = button.split('>')[0]

    if callback_data == 'back_to_problem_type':
        admission.get_problem_type(bot, update)
        return states.GET_PROBLEM_TYPE

    elif callback_data == 'back_to_admission_menu':
        functions.main_menu(bot, update)
        return states.MAIN

    save_data_to_cache(external_id=update.effective_chat.id, data=problem_type, request_name='problem_type')
    if callback_data == 'Communal':
        admission.get_communal_problem(bot, update)
        return states.GET_COMMUNAL_PROBLEM

    elif callback_data == 'land_issues':
        admission.get_land_issues_problem(bot, update)
        return states.GET_LAND_ISSUES_PROBLEM

    elif callback_data == 'social_security':
        admission.get_social_security_problem(bot, update)
        return states.GET_SOCIAL_SECURITY_PROBLEM


