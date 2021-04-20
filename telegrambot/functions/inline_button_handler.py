from django.apps import apps
from telegram import Bot, Update
from telegrambot import functions, states
from telegrambot.functions import admission


def inline_button_handler(bot: Bot, update: Update):
    print('inline_button_handler')

    callback_data = update.callback_query.data

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    if callback_data == 'ru_':
        functions.set_ru(bot, update)

    if callback_data == 'uz_':
        functions.set_uz(bot, update)

    if callback_data == 'admission':
        functions.admission_menu(bot, update)

    if callback_data == 'first_name':
        admission.get_first_name(bot, update)
        return states.GET_FIRST_NAME

    if callback_data == 'last_name':
        admission.get_last_name(bot, update)
        return states.GET_LAST_NAME

    if callback_data == 'middle_name':
        admission.get_middle_name(bot, update)
        return states.GET_MIDDLE_NAME

    if callback_data == 'district':
        admission.get_district(bot, update)
        return states.GET_DISTRICT

    if callback_data == 'problem_type':
        admission.get_problem_type(bot, update)
        return states.GET_PROBLEM_TYPE

    if callback_data == 'back_to_problem_type':
        admission.get_problem_type(bot, update)
        return states.GET_PROBLEM_TYPE

    if callback_data == 'back_to_admission_menu':
        functions.admission_menu(bot, update)
