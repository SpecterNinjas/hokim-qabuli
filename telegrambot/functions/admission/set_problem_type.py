from telegram import Bot, Update

from telegrambot import states
from telegrambot.functions import admission


def set_problem_type(bot: Bot, update: Update):
    print('set_problem_type')

    callback_data = update.callback_query.data

    if callback_data == 'back_to_problem_type':
        admission.get_problem_type(bot, update)
        return states.GET_PROBLEM_TYPE

    elif callback_data == 'Communal':
        admission.get_communal_problem(bot, update)
        return states.GET_COMMUNAL_PROBLEM

    elif callback_data == 'land_issues':
        admission.get_land_issues_problem(bot, update)
        return states.GET_LAND_ISSUES_PROBLEM

    elif callback_data == 'social_security':
        admission.get_social_security_problem(bot, update)
        return states.GET_SOCIAL_SECURITY_PROBLEM
