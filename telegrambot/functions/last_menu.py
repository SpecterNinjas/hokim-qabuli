from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegrambot.models import Text
from telegrambot import states
from telegrambot.apps import log_errors
from panel.models import Murojatchi, Hudud, Mahalla
from telegrambot import models


@log_errors
def last_menu(bot: Bot, update: Update):
    print('main_menu')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    data = Text.objects.filter(text_id='LAST_MENU').values()[0]
    text = data[user.lang]

    request = cache.get(f'request_{update.effective_chat.id}')

    region = models.RegionBot.objects.get(token=bot.token)
    hudud = Hudud.objects.get(title=region.region)

    if user.lang == 'ru':
        mahalla = Mahalla.objects.get(title_ru=request['district'])
    else:
        mahalla = Mahalla.objects.get(title_uz=request['district'])

    applicant = Murojatchi.objects.create(telegram_id=update.effective_chat.id)
    applicant.username = update.effective_chat.username
    applicant.fullname = request['first_name']
    applicant.last_name = request['last_name']
    applicant.middle_name = request['middle_name']
    applicant.year_of_birth = request['year_of_birth']
    applicant.month_of_birth = request['month_of_birth']
    applicant.day_of_birth = request['day_of_birth']
    applicant.gender = request['gender']
    applicant.hudud = hudud
    applicant.mahalla = mahalla
    applicant.murojat_turi = ''
    applicant.muammo = ''
    applicant.category = ''
    applicant.media = ''
    applicant.location = ''
    applicant.description = request['short_description']
    applicant.phone = request['phone_number']
    applicant.save()

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
