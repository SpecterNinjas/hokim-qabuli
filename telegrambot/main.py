from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters

from telegrambot import functions, states
from telegrambot.functions import admission

start_handler = CommandHandler('start', functions.start)
main_handler = CallbackQueryHandler(functions.inline_button_handler)

conv_handler = ConversationHandler(
    entry_points=
    [
        CommandHandler('start', functions.start)
    ],
    states={
        states.GET_LANG: [
            start_handler,
            main_handler,
        ],
        states.STATEMENT_TYPE: [
            start_handler,
            main_handler,
        ],
        states.MAIN: [
            start_handler,
            main_handler,
        ],

        states.GET_NAME: [
            start_handler,
            MessageHandler(Filters.text, admission.set_name),
            main_handler,
        ],
        states.GET_BIRTH_YEAR: [
            start_handler,
            MessageHandler(Filters.regex("(Назад|Orqaga)"), functions.request_menu),
            MessageHandler(Filters.text, admission.set_birth_year),
            main_handler,
        ],
        states.GET_BIRTH_MONTH: [
            start_handler,
            MessageHandler(Filters.regex("(Назад|Orqaga)"), functions.request_menu),
            MessageHandler(Filters.text, admission.set_birth_month),
            main_handler,
        ],
        states.GET_BIRTH_DAY: [
            start_handler,
            MessageHandler(Filters.text, admission.set_birth_day),
            main_handler,
        ],
        states.GET_GENDER: [
            start_handler,
            CallbackQueryHandler(admission.set_gender),
        ],
        states.GET_DISTRICT: [
            start_handler,
            MessageHandler(Filters.regex("(Назад|Orqaga)"), functions.request_menu),
            MessageHandler(Filters.text, admission.set_district),
        ],
        states.GET_PROBLEM_TYPE: [
            start_handler,
            CallbackQueryHandler(admission.set_problem_type),
            main_handler,
        ],
        states.GET_COMMUNAL_PROBLEM: [
            start_handler,
            CallbackQueryHandler(admission.set_communal_problem),
        ],
        states.GET_LAND_ISSUES_PROBLEM: [
            start_handler,
            CallbackQueryHandler(admission.set_land_issues_problem),
        ],
        states.GET_SOCIAL_SECURITY_PROBLEM: [
            start_handler,
            CallbackQueryHandler(admission.set_social_security_problem),
        ],
        states.GET_SHORT_DESCRIPTION: [
            start_handler,
            main_handler,
            MessageHandler(Filters.text, admission.set_short_description),
        ],
        states.GET_PROBLEM_ADDRESS: [
            start_handler,
            MessageHandler(Filters.all, admission.set_problem_address)
        ],
        states.GET_MEDIA: [
            start_handler,
            main_handler,
            MessageHandler(Filters.photo, admission.set_media),
        ],
        states.GET_PHONE_NUMBER: [
            start_handler,
            MessageHandler(Filters.text, admission.set_phone_number),
            MessageHandler(Filters.contact, admission.set_phone_number),
        ],
        states.MAIN_MENU: [
            start_handler,
            MessageHandler(
                Filters.regex(r"Hokim qabuliga yozish|Письмо к приему Хакима|Hokimga murojat|Обращение к Хакиму"),
                functions.application_type_handler),
            MessageHandler(Filters.regex(r"Mening murojatlarim|Мои заявки"), functions.my_appeals_list),
            MessageHandler(Filters.regex(r"Sozlamalar|Настройки"), functions.profile_settings),
            MessageHandler(Filters.regex(r"Mening murojatlarim|Мои заявки"), functions.my_appeals_list),
        ],
        states.PROFILE_SETTINGS: [
            start_handler,
            MessageHandler(Filters.regex(r"Tilni o'zgartirish|Поменять язык"), functions.get_change_language),
            MessageHandler(Filters.regex(r"Profil|Мой профиль"), functions.my_profile),
            MessageHandler(Filters.regex(r"Orqaga|Назад"), functions.main_menu),
        ],
        states.CHANGE_LANGUAGE: [
            start_handler,
            MessageHandler(Filters.regex(r"Русский язык|O'zbek tili"), functions.set_change_language)
        ],
        states.MY_APPEALS_LIST: [
            start_handler,
            CallbackQueryHandler(functions.show_my_appeal),
        ],
    },
    fallbacks=[],
)
