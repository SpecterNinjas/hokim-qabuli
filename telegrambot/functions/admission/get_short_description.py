from telegram import Bot, Update, InlineKeyboardMarkup
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang


@log_errors
def get_short_description(bot: Bot, update: Update):
    print('get_short_description')

    user = get_user_lang(update)

    data = Text.objects.filter(text_id='GET_SHORT_DESCRIPTION').values()[0]
    text = data[user.lang]
    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    bot.delete_message(
        chat_id=update.effective_chat.id,
        message_id=update.callback_query.message.message_id,
    )
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard),
        parse_mode='Markdown',
    )

    return states.GET_SHORT_DESCRIPTION
