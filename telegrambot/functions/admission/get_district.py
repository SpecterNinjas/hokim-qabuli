from django.apps import apps
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup

from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.models import Text
from telegrambot.services import get_user_lang
from telegrambot.services.services import delete_or_send_message


@log_errors
def get_district(bot: Bot, update: Update):
    print('get_district')

    user = get_user_lang(update)

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

    delete_or_send_message(bot, update, keyboard, text)
    return states.GET_DISTRICT
