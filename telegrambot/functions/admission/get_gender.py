from telegram import Bot, Update
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang
from telegrambot.services.services import edit_or_send_message


@log_errors
def get_gender(bot: Bot, update: Update):
    print('get_gender')

    user = get_user_lang(update)
    data = Text.objects.filter(text_id='GET_GENDER').values()[0]
    text = data[user.lang]
    edit_or_send_message(bot, update, inline_keyboard=generate_inline_keyboard(data[f"buttons_{user.lang}"],
                                                                               update.effective_chat.id), text=text)
    return states.GET_GENDER
