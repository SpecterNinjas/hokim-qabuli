from django.apps import apps
from telegram import Bot, Update

from telegrambot import functions


def set_uz(bot: Bot, update: Update):
    print('set_uz')
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)
    user.lang = 'uz'
    user.save()

    bot.delete_message(
        chat_id=update.effective_chat.id,
        message_id=update.callback_query.message.message_id,
    )
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="O'zbek tili tanlandi."
    )

    return functions.statement_type(bot, update)
