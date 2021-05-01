import re
from telegram import Bot, Update
from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang, send_saved_message_text
from telegrambot.services.services import save_data_to_cache, delete_previous_message_with_button


@log_errors
def set_last_name(bot: Bot, update: Update):
    print('set_last_name')

    user = get_user_lang(update.effective_chat.id)

    last_name = update.message.text

    if re.search(r"[0-9]", last_name):
        if user.lang == 'ru':
            err_text = 'Неправильный формат фамилии. Попробуйте еще раз.'
        else:
            err_text = "📝 *Iltimos, familyangizni kiriting:*\n\n" \
                       "❗️_Iltimos, familyangizni kiritishda harflardan foydalaning._"
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=err_text,
            parse_mode='Markdown'
        )
        return states.GET_LAST_NAME

    delete_previous_message_with_button(bot, update.effective_chat.id)
    save_data_to_cache(external_id=update.effective_chat.id, data=last_name, request_name='last_name')
    send_saved_message_text(user, bot, update)

    return functions.admission.get_middle_name(bot, update)
