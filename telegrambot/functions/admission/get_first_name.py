from django.apps import apps
from telegram import Bot, Update, InlineKeyboardMarkup

from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang


@log_errors
def get_first_name(bot: Bot, update: Update):
    print('get_first_name')

    user = get_user_lang(update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_FIRST_NAME').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    bot.edit_message_text(
        chat_id=update.effective_chat.id,
        text=text,
        message_id=update.callback_query.message.message_id,
        reply_markup=InlineKeyboardMarkup(inline_keyboard),
        parse_mode='Markdown'
    )

    return states.GET_FIRST_NAME
