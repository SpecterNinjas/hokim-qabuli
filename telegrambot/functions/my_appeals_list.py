from telegram import Bot, Update, InlineKeyboardButton
from panel.models import Murojatchi
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.services import get_user_lang, edit_or_send_message


@log_errors
def my_appeals_list(bot: Bot, update: Update):
    print('my_appeals')
    user = get_user_lang(update)

    clients = Murojatchi.objects.all().filter(telegram_id=update.effective_chat.id)
    text = "Mening murojatlarim:" if user.lang == 'uz' else 'Мои заявки:'
    back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'
    inline_keyboard = []
    for client in clients:
        inline_keyboard.append([InlineKeyboardButton(str(client.created) + ' ' + client.description,
                                                     callback_data=client.id)])
    inline_keyboard.append([InlineKeyboardButton(back_btn_text, callback_data='back_to_main_menu')])
    edit_or_send_message(bot, update, inline_keyboard, text)
    return states.MY_APPEALS_LIST
