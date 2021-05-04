from telegram import Bot, Update, InlineKeyboardButton
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.models import Text
from telegrambot.services import get_user_lang, edit_or_send_message
from telegrambot.helpers import generate_inline_keyboard
from panel.models import Murojatchi


@log_errors
def get_name(bot: Bot, update: Update):
    print('get_first_name')

    user = get_user_lang(update)
    data = Text.objects.filter(text_id='GET_FULL_NAME').values()[0]
    text = data[user.lang]

    if Murojatchi.objects.filter(telegram_id=update.effective_chat.id).exists():
        inline_keyboard = []
        back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'
        client = Murojatchi.objects.filter(telegram_id=update.effective_chat.id).last()
        inline_keyboard.append([InlineKeyboardButton(client.fullname, callback_data='set_name')])
        inline_keyboard.append([InlineKeyboardButton(back_btn_text, callback_data='back_to_admission_menu')])
    else:
        inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    edit_or_send_message(bot, update, inline_keyboard, text)
    return states.GET_NAME
