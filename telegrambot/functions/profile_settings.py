from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegrambot import states
from telegrambot.services import get_user_lang


def profile_settings(bot: Bot, update: Update):
    print('profile_settings')
    user = get_user_lang(update)
    keyboard = []
    lang_text = "Tilni o'zgartirish" if user.lang == 'uz' else 'Поменять язык'
    my_profile = "Profil" if user.lang == 'uz' else 'Мой профиль'
    back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'

    keyboard.append([KeyboardButton(lang_text)])
    keyboard.append([KeyboardButton(my_profile)])
    keyboard.append([KeyboardButton(back_btn_text)])
    bot.send_message(
        chat_id=update.effective_chat.id,
        text='1',
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
    )
    return states.PROFILE_SETTINGS
