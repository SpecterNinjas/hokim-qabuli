from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
from panel.models import Murojatchi
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang, edit_or_send_message


@log_errors
def get_birth_month(bot: Bot, update: Update):
    print('get_birth_month')

    user = get_user_lang(update)

    data = Text.objects.filter(text_id='GET_BIRTH_MONTH').values()[0]
    text = data[user.lang]

    keyboard = generate_keyboard(data[f"buttons_{user.lang}"])
    back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'
    keyboard.append([KeyboardButton(back_btn_text)])

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    )
    if Murojatchi.objects.filter(telegram_id=update.effective_chat.id).exists():
        inline_keyboard = []
        client = Murojatchi.objects.filter(telegram_id=update.effective_chat.id).last()
        inline_keyboard.append([InlineKeyboardButton(client.month_of_birth, callback_data='set_month_of_birth')])
        edit_or_send_message(bot, update, inline_keyboard, text)
    return states.GET_BIRTH_MONTH
