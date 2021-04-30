from django.apps import apps
from telegram import Bot, Update, InlineKeyboardMarkup
from telegrambot.services import get_user_lang
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text


@log_errors
def get_last_name(bot: Bot, update: Update):
    print('get_last_name')

    user = get_user_lang(update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_LAST_NAME').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    try:
        bot.edit_message_text(
            chat_id=update.effective_chat.id,
            text=text,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
            parse_mode='Markdown'
        )
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
            parse_mode='Markdown',
        )
    return states.GET_LAST_NAME
