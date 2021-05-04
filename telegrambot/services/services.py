from django.apps import apps
from django.core.cache import cache
from telegram import Update, Bot, InlineKeyboardMarkup, ReplyKeyboardMarkup


def get_user_lang(update: Update):
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)
    return user


def send_saved_message_text(user, bot: Bot, update: Update):
    if user.lang == 'uz':
        text = 'Saqlandi'
    else:
        text = 'Сохранено'

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


def save_data_to_cache(update: Update, data, request_name):
    request = cache.get(f'request_{update.effective_chat.id}')
    request[f'{request_name}'] = data
    cache.set(f'request_{update.effective_chat.id}', request)


def delete_previous_message_with_button(bot: Bot, update: Update, request_name):
    request = cache.get(f'request_{update.effective_chat.id}')
    bot.delete_message(
        chat_id=update.effective_chat.id,
        message_id=request[f'{request_name}'],
    )


def edit_or_send_message(bot: Bot, update: Update, inline_keyboard, text):
    try:
        msg = bot.edit_message_text(
            chat_id=update.effective_chat.id,
            text=text,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
            parse_mode='HTML'
        )
    except:
        msg = bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
            parse_mode='HTML',
        )
    save_data_to_cache(update, msg.message_id, request_name='callback_message_id')


def delete_or_send_message(bot: Bot, update: Update, keyboard, text):
    try:
        bot.delete_message(
            chat_id=update.effective_chat.id,
            message_id=update.callback_query.message.message_id,
        )
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
            parse_mode='Markdown'
        )
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True),
            parse_mode='Markdown',
        )
