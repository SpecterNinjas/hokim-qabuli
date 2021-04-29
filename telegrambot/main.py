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

        states.GET_FIRST_NAME: [
            start_handler,
            MessageHandler(Filters.text, admission.set_first_name),
            main_handler,
        ],
        states.GET_LAST_NAME: [
            start_handler,
            MessageHandler(Filters.text, admission.set_last_name),
            main_handler,
        ],
        states.GET_MIDDLE_NAME: [
            start_handler,
            MessageHandler(Filters.text, admission.set_middle_name),
            main_handler,
        ],
        states.GET_DISTRICT: [
            start_handler,
            MessageHandler(Filters.regex("(Назад|Orqaga)"), functions.main_menu),
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
        states.GET_FILE: [
            start_handler,
            main_handler,
            MessageHandler(Filters.all, admission.set_file),
        ],
        states.GET_LOCATION: [
            start_handler,
            main_handler,
            MessageHandler(Filters.all, admission.set_location),
        ],
        states.GET_PHONE_NUMBER: [
            start_handler,
            MessageHandler(Filters.contact, admission.set_phone_number),
        ],
    },
    fallbacks=[],
)
