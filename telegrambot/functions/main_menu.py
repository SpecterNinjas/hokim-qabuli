from django.core.cache import cache
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegrambot.models import Text
from telegrambot import states
from telegrambot.apps import log_errors
from panel.models import Murojatchi, Hudud, Mahalla
from telegrambot import models
from telegrambot.services import get_user_lang, delete_or_send_message


@log_errors
def main_menu(bot: Bot, update: Update):
    print('main_menu')

    user = get_user_lang(update)

    data = Text.objects.filter(text_id='LAST_MENU').values()[0]
    text = data[user.lang]

    request = cache.get(f'request_{update.effective_chat.id}')

    # region = models.RegionBot.objects.get(token=bot.token)
    # hudud = Hudud.objects.get(title=region.region)
    #
    # if user.lang == 'ru':
    #     mahalla = Mahalla.objects.get(title_ru=request['district'])
    # else:
    #     mahalla = Mahalla.objects.get(title_uz=request['district'])
    #
    # applicant = Murojatchi.objects.create(telegram_id=update.effective_chat.id)
    # applicant.murojat_turi = request['request_type']
    # applicant.username = update.effective_chat.username
    # applicant.fullname = request['name']
    # applicant.year_of_birth = request['year_of_birth']
    # applicant.month_of_birth = request['month_of_birth']
    # applicant.day_of_birth = request['day_of_birth']
    # applicant.gender = request['gender']
    # applicant.hudud = hudud
    # applicant.mahalla = mahalla
    # # applicant.muammo = request['problem_type']
    # # applicant.category = request['sub_problem']
    # # applicant.media = ''
    # # applicant.location = ''
    # applicant.description = request['short_description']
    # applicant.phone = request['phone_number']
    # applicant.save()

    keyboard = []
    admissions_text = "✍️ Hokim qabuliga yozish" if user.lang == 'uz' else '✍️ Письмо к приему Хакима'
    appeal_text = "📝 Hokimga murojat" if user.lang == 'uz' else '📝 Обращение к Хакиму'
    my_appeals = "📖 Mening murojatlarim" if user.lang == 'uz' else '📖 Мои заявки'
    settings = "⚙️ Sozlamalar" if user.lang == 'uz' else '⚙️ Настройки'

    keyboard.append([KeyboardButton(admissions_text)])
    keyboard.append([KeyboardButton(appeal_text)])
    keyboard.append([KeyboardButton(my_appeals)])
    keyboard.append([KeyboardButton(settings)])
    delete_or_send_message(bot, update, keyboard, text)

    return states.MAIN_MENU
