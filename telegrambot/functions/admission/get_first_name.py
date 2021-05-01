from telegram import Bot, Update
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.models import Text
from telegrambot.services import get_user_lang, edit_or_send_message
from panel.models import Murojatchi
from telegrambot.services.services import get_suggestion_button


@log_errors
def get_first_name(bot: Bot, update: Update):
    print('get_first_name')

    user = get_user_lang(update.effective_chat.id)
    data = Text.objects.filter(text_id='GET_FIRST_NAME').values()[0]
    text = data[user.lang]

    client = Murojatchi.objects.filter(telegram_id=update.effective_chat.id).last()
    inline_keyboard = get_suggestion_button(update, model_field=client.fullname, callback_data='set_name')

    edit_or_send_message(bot, update, text, inline_keyboard)

    return states.GET_FIRST_NAME
