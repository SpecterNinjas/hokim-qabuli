from django.apps import apps
from django.core.cache import cache
from telegram import Update, Bot, ReplyKeyboardRemove

from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import send_saved_message_text


@log_errors
def set_birth_year(bot: Bot, update: Update):
    print('set_birth_year')
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    birth_year = update.message.text

    if int(birth_year) not in range(1970, 2013):
        if user.lang == 'ru':
            text = 'Вы ввели некорректный год рождения. Попробуйте еще раз'
        else:
            text = "👇🏻 *Yil tanlang:*:\n\n❗️quyidagi tugmalardan foydalaning"
        bot.send_message(
            chat_id=update.effective_chat.id, text=text, parse_mode='Markdown')
        return states.GET_BIRTH_YEAR

    request = cache.get(f'request_{update.effective_chat.id}')
    request['year_of_birth'] = birth_year
    cache.set(f'request_{update.effective_chat.id}', request)

    send_saved_message_text(user, bot, update)
    return admission.get_birth_month(bot, update)
