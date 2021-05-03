from telegram import Bot, Update
from telegrambot import functions
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang


@log_errors
def set_ru(bot: Bot, update: Update):
    print('set_ru')
    user = get_user_lang(update.effective_chat.id)
    user.lang = 'ru'
    user.save()
    bot.delete_message(
        chat_id=update.effective_chat.id,
        message_id=update.callback_query.message.message_id,
    )
    bot.send_message(
        chat_id=update.effective_chat.id,
        text='Выбран русский язык.'
    )

    return functions.main_menu(bot, update)
