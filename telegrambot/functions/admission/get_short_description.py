from django.apps import apps
from telegram import Bot, Update, InlineKeyboardMarkup
from telegrambot.models import Text
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard


@log_errors
def get_short_description(bot: Bot, update: Update):
    print('get_short_description')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_SHORT_DESCRIPTION').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    try:
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
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
            parse_mode='Markdown',
        )

    return states.GET_SHORT_DESCRIPTION
