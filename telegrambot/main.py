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
            MessageHandler(Filters.regex("(Назад|Orqaga)"), functions.admission_menu),
            MessageHandler(Filters.text, admission.set_district),
        ],
        states.GET_PROBLEM_TYPE: [
            start_handler,
            CallbackQueryHandler(admission.set_problem_type),
            main_handler,
        ],
        states.GET_COMMUNAL_PROBLEM: [
            start_handler,
            main_handler,
            CallbackQueryHandler(admission.set_communal_problem),
        ],
        states.GET_SHORT_DESCRIPTION: [
            start_handler,
            main_handler,
            MessageHandler(Filters.text, admission.set_short_description),
        ],
    },
    fallbacks=[],
)
