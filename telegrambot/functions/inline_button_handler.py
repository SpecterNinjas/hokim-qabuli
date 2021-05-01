from django.apps import apps
from telegram import Bot, Update
from telegrambot import functions, states
from telegrambot.functions import admission


def inline_button_handler(bot: Bot, update: Update):
    print('inline_button_handler')

    callback_data = update.callback_query.data

    if callback_data == 'ru_':
        functions.set_ru(bot, update)

    if callback_data == 'uz_':
        functions.set_uz(bot, update)

    if callback_data == 'admission' or callback_data == 'appeal':
        functions.main_menu(bot, update)
        return states.MAIN

    # ---ADMISSION MENU BUTTONS HANDLERS--- #
    if callback_data == 'first_name':
        admission.get_first_name(bot, update)
        return states.GET_FIRST_NAME

    if callback_data == 'last_name':
        admission.get_last_name(bot, update)
        return states.GET_LAST_NAME

    if callback_data == 'middle_name':
        admission.get_middle_name(bot, update)
        return states.GET_MIDDLE_NAME

    if callback_data == 'date_of_birth':
        admission.get_birth_year(bot, update)
        return states.GET_BIRTH_YEAR

    if callback_data == 'gender':
        admission.get_gender(bot, update)
        return states.GET_GENDER

    if callback_data == 'district':
        admission.get_district(bot, update)
        return states.GET_DISTRICT

    if callback_data == 'problem_type':
        admission.get_problem_type(bot, update)
        return states.GET_PROBLEM_TYPE

    if callback_data == 'short_description':
        admission.get_short_description(bot, update)
        return states.GET_SHORT_DESCRIPTION

    if callback_data == 'problem_address':
        admission.get_problem_address(bot, update)
        return states.GET_PROBLEM_ADDRESS

    if callback_data == 'media':
        admission.get_media(bot, update)
        return states.GET_MEDIA

    if callback_data == 'phone_number':
        admission.get_phone_number(bot, update)
        return states.GET_PHONE_NUMBER
    # ---------------------------------------- #

    # ----------SUGGESTION SETTERS------------ #
    if callback_data == 'set_first_name':
        pass
    if callback_data == 'set_last_name':
        pass
    if callback_data == 'set_middle_name':
        pass
    if callback_data == 'set_set_year_of_birth':
        pass
    if callback_data == 'set_set_day_of_birth':
        pass
    # ---------------------------------------- #

    if callback_data == 'back_to_problem_type':
        admission.get_problem_type(bot, update)
        return states.GET_PROBLEM_TYPE

    if callback_data == 'back_to_admission_menu':
        functions.main_menu(bot, update)
        return states.MAIN

    if callback_data == 'back_to_statement_type':
        functions.statement_type(bot, update)
        return states.STATEMENT_TYPE

    if callback_data == 'skip_file':
        admission.get_location(bot, update)
        return states.GET_LOCATION

    if callback_data == 'skip_location':
        admission.get_phone_number(bot, update)
        return states.GET_PHONE_NUMBER

    if callback_data == 'save_admission_info':
        functions.last_menu(bot, update)
