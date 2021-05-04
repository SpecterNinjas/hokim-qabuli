from django.apps import apps
from telegram import Bot, Update
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import send_saved_message_text, save_data_to_cache, get_user_lang


@log_errors
def set_birth_month(bot: Bot, update: Update):
    print('set_birth_month')

    user = get_user_lang(update)
    try:
        callback = update.callback_query.message.reply_markup.inline_keyboard[0][0]
        month_of_birth = callback.text
    except:
        month_of_birth = update.message.text
        if user.lang == 'ru':
            months = apps.get_model('telegrambot', 'Month').objects.all(
            ).values_list('title_ru', flat=True)
        else:
            months = apps.get_model('telegrambot', 'Month').objects.all(
            ).values_list('title_uz', flat=True)

        if month_of_birth not in months:
            if user.lang == 'ru':
                text = 'Вы ввели некорректный месяц рождения. Попробуйте еще раз'
            else:
                text = "👇🏻 *Oy tanlang:*:\n\n❗️quyidagi tugmalardan foydalaning"
            bot.send_message(
                chat_id=update.effective_chat.id, text=text, parse_mode='Markdown')
            return states.GET_BIRTH_MONTH

    save_data_to_cache(update, month_of_birth, request_name='month_of_birth')
    send_saved_message_text(user, bot, update)
    return admission.get_birth_day(bot, update)
