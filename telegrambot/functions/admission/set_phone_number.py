import re
from telegram import Bot, Update
from telegrambot import functions, states
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang, send_saved_message_text, save_data_to_cache


@log_errors
def set_phone_number(bot: Bot, update: Update):
    print('set_phone_number')
    user = get_user_lang(update.effective_chat.id)

    try:
        save_data_to_cache(external_id=update.effective_chat.id, data=update.message.contact.phone_number,
                           request_name='phone_number')
    except:
        phone_number = update.message.text
        if re.search(r"^\d{7}$", phone_number):
            save_data_to_cache(external_id=update.effective_chat.id, data=phone_number,
                               request_name='phone_number')
        else:
            if user.lang == 'ru':
                err_text = 'Неправильный формат номера телефона. Попробуйте еще раз.'
            else:
                err_text = "📝 *Telefon raqamni shakli noto'g'ri. Yana bir bor urinib ko `ring.:"
            bot.send_message(
                chat_id=update.effective_chat.id,
                text=err_text,
            )
            return states.GET_PHONE_NUMBER
    send_saved_message_text(user, bot, update)
    return functions.main_menu(bot, update)

# {problem_address_sign}Muammo yuzaga kelgan joy: {problem_address}
# Muammo yuzaga kelgan joy>problem_address|
# Место происшествия>problem_address|
# {problem_address_sign}Место происшествия: {problem_address}
