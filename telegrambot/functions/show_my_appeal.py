from telegram import Bot, Update
from panel.models import Murojatchi
from telegrambot import states, functions
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang, edit_or_send_message


@log_errors
def show_my_appeal(bot: Bot, update: Update):
    print('show_my_appeal')
    user = get_user_lang(update)
    if update.callback_query.data == 'back_to_main_menu':
        return functions.main_menu(bot, update)
    applicant = Murojatchi.objects.get(id=update.callback_query.data)

    data = Text.objects.filter(text_id='SHOW_MY_APPEAL').values()[0]
    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)
    text = data[user.lang].format(
        created_sign='🕰️ ', created=applicant.created,
        problem_type_sign='✅️ ', problem_type=applicant.muammo,
        sub_problem_sign='✅️ ', sub_problem=applicant.category,
        short_description_sign='✅️ ', short_description=applicant.description,
        problem_address_sign='✅️ ', problem_address=applicant.location,
    )
    edit_or_send_message(bot, update, inline_keyboard, text)
    return states.MAIN

