from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update

from telegrambot.apps import text_manager, log_errors
from telegrambot.functions import admission


@log_errors
def set_land_issues_problem(bot: Bot, update: Update):
    print('set_land_issues')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    data = text_manager.objects.filter(text_id='GET_LAND_ISSUES_PROBLEM').values()[0]
    callback_data = update.callback_query.data

    texts = data[f"buttons_{user.lang}"].splitlines()

    for text in texts:
        buttons = text.split('|')
        for button in buttons:
            if callback_data == button.split('>')[1]:
                sub_problem = button.split('>')[0]

    if callback_data == 'back_to_problem_type':
        return admission.get_problem_type(bot, update)

    request = cache.get(f'request_{update.effective_chat.id}')
    request['sub_problem'] = sub_problem
    cache.set(f'request_{update.effective_chat.id}', request)

    if user.lang == 'uz':
        text = 'Saqlandi'
    else:
        text = 'Сохранено'

    bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
    )
    return admission.get_short_description(bot, update)