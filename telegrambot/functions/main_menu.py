from django.apps import apps
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup

from telegrambot import states
from telegrambot.apps import log_errors


@log_errors
def main_menu(bot: Bot, update: Update):
    print('main_menu')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    data = Text.objects.filter(text_id='MAIN_MENU').values()[0]
    text = data[user.lang]

    keyboard = []
    my_admissions_text = "Murojatlar" if user.lang == 'uz' else 'Заявки'
    lang_text = "Tilni o'zgartirish" if user.lang == 'uz' else 'Поменять язык'

    keyboard.append([KeyboardButton(my_admissions_text)])
    keyboard.append([KeyboardButton(lang_text)])
    try:
        bot.delete_message(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
        )
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
        )
    return states.MAIN_MENU
