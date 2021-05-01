from django.apps import apps
from django.core.cache import cache
from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from panel.models import Murojatchi


def get_user_lang(external_id):
    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=external_id)
    return user


def send_saved_message_text(user: get_user_lang, bot: Bot, update: Update):
    if user.lang == 'uz':
        text = 'Saqlandi'
    else:
        text = 'Сохранено'

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )


def save_data_to_cache(external_id, data, request_name):
    request = cache.get(f'request_{external_id}')
    request[f'{request_name}'] = data
    cache.set(f'request_{external_id}', request)


def edit_or_send_message(bot: Bot, update: Update, text, inline_keyboard):
    try:
        msg = bot.edit_message_text(
            chat_id=update.effective_chat.id,
            text=text,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
            parse_mode='Markdown'
        )
    except:
        msg = bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
            parse_mode='Markdown',
        )
    save_data_to_cache(external_id=update.effective_chat.id, data=msg.message_id, request_name='callback_message_id')


def delete_previous_message_with_button(bot: Bot, external_id):
    request = cache.get(f'request_{external_id}')
    bot.delete_message(
        chat_id=external_id,
        message_id=request['callback_message_id'],
    )


def download_cache_data(update: Update):
    applicant = Murojatchi.objects.filter(telegram_id=update.effective_chat.id).last()
    request = cache.get(f'request_{update.effective_chat.id}')
    request['last_name'] = applicant.last_name
    request['middle_name'] = applicant.last_name
    request['year_of_birth'] = applicant.year_of_birth
    request['month_of_birth'] = applicant.month_of_birth
    request['day_of_birth'] = applicant.day_of_birth
    request['phone_number'] = applicant.phone
    cache.set(f'request_{update.effective_chat.id}', request)

# def get_suggestion_button(update: Update, model_field, callback_data, user):
#
#     inline_keyboard = []
#     if Murojatchi.objects.filter(telegram_id=update.effective_chat.id).exists():
#         inline_keyboard.append(
#             [
#                 InlineKeyboardButton(model_field, callback_data=f'{callback_data}')
#             ]
#         )
#     btn_text = '⬅Orqaga' if user.lang == 'uz' else '⬅Назад'
#     inline_keyboard.append(
#         [
#             InlineKeyboardButton(btn_text, callback_data='back_to_admission_menu')
#         ]
#     )
#     return inline_keyboard
