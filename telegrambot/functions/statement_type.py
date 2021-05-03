from django.apps import apps
from telegram import Update, Bot, InlineKeyboardMarkup

from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard


@log_errors
def statement_type(bot: Bot, update: Update):
    print('statement_type')
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    Text = apps.get_model('telegrambot', 'Text')
    data = Text.objects.filter(text_id='STATEMENT_TYPE').values()[0]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)
    text = data[user.lang]
    try:
        bot.delete_message(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id
        )
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=InlineKeyboardMarkup(inline_keyboard)
        )
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=InlineKeyboardMarkup(inline_keyboard)
        )
    return states.STATEMENT_TYPE
