from telegram import Bot, Update
from telegrambot.apps import log_errors
from telegrambot.helpers import generate_inline_keyboard
from telegrambot.models import Text
from telegrambot.services import get_user_lang
from panel.models import ProfileSuggestion


@log_errors
def my_profile(bot: Bot, update: Update):
    print('my_profile')
    user = get_user_lang(update)

    data = Text.objects.filter(text_id='SHOW_MY_APPEAL').values()[0]
    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)
    # applicant = ProfileSuggestion.objects.get(telegram_id=update.effective_chat.id)
    # text = data[user.lang].format(
    #     name_sign='🕰️ ', name=applicant.fullname,
    #     date_of_birth_sign='✅️ ', date_of_birth=applicant.muammo,
    #     gender_sign='✅️ ', gender=applicant.gender,
    #     phone_number_sign='✅️ ', phone_number=applicant.phone,
    # )
    bot.send_message(
        chat_id=update.effective_chat.id,
        text='text',
    )
