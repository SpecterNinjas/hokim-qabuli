from telegram import Update, Bot

from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import send_saved_message_text
from telegrambot.services.services import save_data_to_cache, get_user_lang, delete_previous_message_with_button


@log_errors
def set_birth_year(bot: Bot, update: Update):
    print('set_birth_year')

    user = get_user_lang(update.effective_chat.id)
    year_of_birth = update.message.text

    if int(year_of_birth) not in range(1970, 2013):
        if user.lang == 'ru':
            text = 'Вы ввели некорректный год рождения. Попробуйте еще раз'
        else:
            text = "👇🏻 *Yil tanlang:*:\n\n❗️quyidagi tugmalardan foydalaning"
        bot.send_message(
            chat_id=update.effective_chat.id, text=text, parse_mode='Markdown')
        return states.GET_BIRTH_YEAR

    delete_previous_message_with_button(bot, update.effective_chat.id)
    save_data_to_cache(external_id=update.effective_chat.id, data=year_of_birth, request_name='year_of_birth')
    send_saved_message_text(user, bot, update)

    return admission.get_birth_month(bot, update)
