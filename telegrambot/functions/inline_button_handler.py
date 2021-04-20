from django.apps import apps
from telegram import Bot, Update
from telegrambot import functions


def inline_button_handler(bot: Bot, update: Update):
    print('inline_button_handler')

    callback_data = update.callback_query.data

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    if callback_data == 'ru_':
        functions.set_ru(bot, update)
    if callback_data == 'uz_':
        functions.set_uz(bot, update)
    if callback_data == 'admission':
        functions.admission_menu(bot, update)

    if callback_data == 'first_name':
        pass