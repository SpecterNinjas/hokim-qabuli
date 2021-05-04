import re
from telegram import Update, Bot
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import send_saved_message_text, save_data_to_cache, get_user_lang, \
    delete_previous_message_with_button


@log_errors
def set_birth_day(bot: Bot, update: Update):
    print('set_birth_day')
    try:
        callback = update.callback_query.message.reply_markup.inline_keyboard[0][0]
        day_of_birth = callback.text
    except:
        day_of_birth = update.message.text
        if re.search(r"[^\d{2}$]", day_of_birth) or int(day_of_birth) not in range(1, 32):
            if get_user_lang(update).lang == 'ru':
                text = 'Вы ввели некорректный день рождения. Попробуйте еще раз'
            else:
                text = "👇🏻 *Tug'ilgan kuningizni kirgizing:"
            bot.send_message(
                chat_id=update.effective_chat.id, text=text, parse_mode='Markdown')
            return states.GET_BIRTH_DAY

    save_data_to_cache(update, day_of_birth, request_name='day_of_birth')
    send_saved_message_text(get_user_lang(update), bot, update)
    delete_previous_message_with_button(bot, update, request_name='callback_message_id')
    return admission.get_gender(bot, update)
