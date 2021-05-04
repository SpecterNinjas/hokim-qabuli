from telegram import Bot, Update, KeyboardButton, InlineKeyboardButton

from panel.models import Murojatchi
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.models import Text
from telegrambot.services import get_user_lang
from telegrambot.services.services import delete_or_send_message, edit_or_send_message


@log_errors
def get_phone_number(bot: Bot, update: Update):
    print('get_phone_number')

    user = get_user_lang(update)
    data = Text.objects.filter(text_id='GET_PHONE_NUMBER').values()[0]

    if user.lang == 'ru':
        keyboard = [
            [KeyboardButton('☎Поделиться номером', request_contact=True)]
        ]
    else:
        keyboard = [
            [KeyboardButton('☎Raqamni ulashish', request_contact=True)]
        ]
    delete_or_send_message(bot, update, keyboard, text=data[user.lang])

    if Murojatchi.objects.filter(telegram_id=update.effective_chat.id).exists():
        inline_keyboard = []
        back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'
        client = Murojatchi.objects.filter(telegram_id=update.effective_chat.id).last()
        inline_keyboard.append([InlineKeyboardButton(client.phone, callback_data='set_phone_number')])
        inline_keyboard.append([InlineKeyboardButton(back_btn_text, callback_data='back_to_admission_menu')])
        edit_or_send_message(bot, update, inline_keyboard, text=data[user.lang])
    return states.GET_PHONE_NUMBER
