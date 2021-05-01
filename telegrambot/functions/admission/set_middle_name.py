import re
from telegram import Bot, Update
from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang, send_saved_message_text
from telegrambot.services.services import save_data_to_cache, delete_previous_message_with_button


@log_errors
def set_middle_name(bot: Bot, update: Update):
    print('set_middle_name')

    user = get_user_lang(update.effective_chat.id)
    middle_name = update.message.text

    if re.search(r"[0-9]", middle_name):
        if user.lang == 'ru':
            err_text = 'Неправильный формат отчества. Попробуйте еще раз.'
        else:
            err_text = "📝 *Iltimos, sharfingizni kiriting:*\n\n" \
                       "❗️_Iltimos, sharfingizni kiritishda harflardan foydalaning._"
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=err_text,
            parse_mode='Markdown'
        )
        return states.GET_MIDDLE_NAME

    save_data_to_cache(external_id=update.effective_chat.id, data=middle_name, request_name='middle_name')
    delete_previous_message_with_button(bot, update.effective_chat.id)
    send_saved_message_text(user, bot, update)

    return functions.admission.get_birth_year(bot, update)
