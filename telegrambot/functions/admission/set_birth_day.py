import re
from django.apps import apps
from django.core.cache import cache
from telegram import Update, Bot
from telegrambot import states
from telegrambot.apps import log_errors


@log_errors
def set_birth_day(bot: Bot, update: Update):
    print('set_birth_day')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    birth_day = update.message.text
    if re.search(r"[^\d{2}$]", birth_day) or int(birth_day) not in range(1, 32):
        if user.lang == 'ru':
            text = 'Вы ввели некорректный день рождения. Попробуйте еще раз'
        else:
            text = "👇🏻 *Tug'ilgan kuningizni kirgizing:"
        bot.send_message(
            chat_id=update.effective_chat.id, text=text, parse_mode='Markdown')
        return states.GET_BIRTH_DAY

    request = cache.get(f'request_{update.effective_chat.id}')
    request['day_of_birth'] = birth_day
    cache.set(f'request_{update.effective_chat.id}', request)

    if user.lang == 'uz':
        text = 'Saqlandi'
    else:
        text = 'Сохранено'
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )
