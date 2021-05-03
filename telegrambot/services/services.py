from django.apps import apps
from telegram import Update, Bot


def get_user_lang(update: Update):
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)
    return user


def send_saved_message_text(user, bot: Bot, update: Update):
    if user.lang == 'uz':
        text = 'Saqlandi'
    else:
        text = 'Сохранено'

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


def save_data_to_cache(update: Update, data, request_name):
    pass


def delete_previous_message_with_button(bot: Bot, update: Update):
    pass
