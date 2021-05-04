from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang


@log_errors
def get_change_language(bot: Bot, update: Update):
    print('get_change_language')
    user = get_user_lang(update)
    keyboard = []
    russian_language = "Русский язык"
    uzbek_language = "O'zbek tili"
    back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'

    keyboard.append([KeyboardButton(russian_language)])
    keyboard.append([KeyboardButton(uzbek_language)])
    keyboard.append([KeyboardButton(back_btn_text)])
    bot.send_message(
        chat_id=update.effective_chat.id,
        text='1',
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
    )
    return states.CHANGE_LANGUAGE
