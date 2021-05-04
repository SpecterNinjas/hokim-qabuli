from telegram import Bot, Update
from telegrambot.services import delete_previous_message_with_button


def set_media(bot: Bot, update: Update):
    print('set_media')
    print(update.message)
    delete_previous_message_with_button(bot, update, request_name='callback_message_id')
