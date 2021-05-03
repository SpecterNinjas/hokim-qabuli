from django.apps import apps
from telegram import Update, Bot, InlineKeyboardMarkup
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text


@log_errors
def get_birth_day(bot: Bot, update: Update):
    print('get_birth_day')
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)
    data = Text.objects.filter(text_id='GET_BIRTH_DAY').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=InlineKeyboardMarkup(inline_keyboard)
    )
    return states.GET_BIRTH_DAY
