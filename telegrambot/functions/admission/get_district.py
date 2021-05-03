from django.apps import apps
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup

from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.models import Text


@log_errors
def get_district(bot: Bot, update: Update):
    print('get_district')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    districts = apps.get_model('panel', 'Mahalla').objects.all().order_by('title')

    data = Text.objects.filter(text_id='GET_DISTRICT').values()[0]
    text = data[user.lang]

    keyboard = []
    back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'
    keyboard.append([KeyboardButton(back_btn_text)])

    for district in districts:
        if user.lang == 'uz':
            keyboard.append([KeyboardButton(district.title_uz)])
        else:
            keyboard.append([KeyboardButton(district.title_ru)])

    try:
        bot.delete_message(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
        )
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        )
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        )
    return states.GET_DISTRICT
