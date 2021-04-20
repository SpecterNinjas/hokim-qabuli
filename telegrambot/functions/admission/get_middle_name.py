from django.apps import apps
from telegram import Bot, Update, InlineKeyboardMarkup

from telegrambot import states
from telegrambot.apps import text_manager, log_errors
from telegrambot.helpers import generate_inline_keyboard


@log_errors
def get_middle_name(bot: Bot, update: Update, edit: bool = True):
    print('get_middle_name')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    data = text_manager.objects.filter(text_id='GET_MIDDLE_NAME').values()[0]
    text = data[user.lang]

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    if edit:
        bot.edit_message_text(chat_id=update.effective_chat.id, text=text,
                              message_id=update.callback_query.message.message_id,
                              reply_markup=InlineKeyboardMarkup(inline_keyboard),
                              parse_mode='Markdown')
    else:
        bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode='Markdown',
                         reply_markup=InlineKeyboardMarkup(inline_keyboard))
    return states.GET_MIDDLE_NAME
