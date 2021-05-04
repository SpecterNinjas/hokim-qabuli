from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from panel.models import Murojatchi
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang, edit_or_send_message


@log_errors
def get_birth_day(bot: Bot, update: Update):
    print('get_birth_day')
    user = get_user_lang(update)

    data = Text.objects.filter(text_id='GET_BIRTH_DAY').values()[0]
    text = data[user.lang]

    if Murojatchi.objects.filter(telegram_id=update.effective_chat.id).exists():
        inline_keyboard = []
        back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'
        client = Murojatchi.objects.filter(telegram_id=update.effective_chat.id).last()
        inline_keyboard.append([InlineKeyboardButton(client.day_of_birth, callback_data='set_day_of_birth')])
        inline_keyboard.append([InlineKeyboardButton(back_btn_text, callback_data='back_to_admission_menu')])
    else:
        inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    edit_or_send_message(bot, update, inline_keyboard, text)
    return states.GET_BIRTH_DAY
