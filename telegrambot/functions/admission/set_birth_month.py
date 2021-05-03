from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update, ReplyKeyboardRemove

from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.functions import admission


@log_errors
def set_birth_month(bot: Bot, update: Update):
    print('set_birth_month')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    birth_month = update.message.text

    if user.lang == 'ru':
        months = apps.get_model('telegrambot', 'Month').objects.all(
        ).values_list('title_ru', flat=True)
    else:
        months = apps.get_model('telegrambot', 'Month').objects.all(
        ).values_list('title_uz', flat=True)

    if birth_month not in months:
        if user.lang == 'ru':
            text = 'Вы ввели некорректный месяц рождения. Попробуйте еще раз'
        else:
            text = "👇🏻 *Oy tanlang:*:\n\n❗️quyidagi tugmalardan foydalaning"
        bot.send_message(
            chat_id=update.effective_chat.id, text=text, parse_mode='Markdown')
        return states.GET_BIRTH_MONTH

    request = cache.get(f'request_{update.effective_chat.id}')
    request['month_of_birth'] = birth_month
    cache.set(f'request_{update.effective_chat.id}', request)

    if user.lang == 'uz':
        text = 'Saqlandi'
    else:
        text = 'Сохранено'

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=ReplyKeyboardRemove()
    )
    return admission.get_birth_day(bot, update)
