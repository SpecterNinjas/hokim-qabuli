from django.apps import apps
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.models import Text


@log_errors
def get_birth_month(bot: Bot, update: Update):
    print('get_birth_month')
    months = apps.get_model('telegrambot', 'Month').objects.all().order_by('id')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    data = Text.objects.filter(text_id='GET_BIRTH_MONTH').values()[0]
    text = data[user.lang]

    keyboard = []

    back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'
    keyboard.append([KeyboardButton(back_btn_text)])

    for month in months:
        if user.lang == 'uz':
            keyboard.append([KeyboardButton(month.title_uz)])
        else:
            keyboard.append([KeyboardButton(month.title_ru)])

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    )
    return states.GET_BIRTH_MONTH
