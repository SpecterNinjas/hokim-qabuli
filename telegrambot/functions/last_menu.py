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

    m = Murojatchi.objects.create(telegram_id=update.effective_chat.id)
    m.fullname = request['first_name'] + request['last_name'] + request['middle_name']
    m.username = update.effective_chat.username
    m.hudud = hudud
    m.mahalla = mahalla
    # m.murojat_turi = ''
    # m.muammo = ''
    # m.category = ''
    # m.media = ''
    # m.location = ''
    m.description = request['short_description']
    m.phone = request['phone_number']
    m.save()

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
