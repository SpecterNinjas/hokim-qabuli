from telegram import Bot, Update, InlineKeyboardMarkup

from telegrambot import states
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang


def get_problem_type(bot: Bot, update: Update):
    print('get_problem_type')

    user = get_user_lang(update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_PROBLEM_TYPE').values()[0]
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
    return states.GET_PROBLEM_TYPE
