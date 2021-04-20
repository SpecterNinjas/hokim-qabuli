from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler

from telegrambot import functions, states

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
    },
    fallbacks=[],
)
