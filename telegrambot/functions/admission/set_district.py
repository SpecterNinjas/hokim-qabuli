from django.apps import apps
from telegram import Bot, Update
from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.functions import admission
from telegrambot.services import send_saved_message_text, save_data_to_cache


@log_errors
def set_district(bot: Bot, update: Update):
    print('set_district')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)

    district = update.message.text

    if user.lang == 'ru':
        districts = apps.get_model('panel', 'Mahalla').objects.filter(token=bot.token).values_list('title_ru',
                                                                                                   flat=True)
    else:
        districts = apps.get_model('panel', 'Mahalla').objects.filter(token=bot.token).values_list('title_uz',
                                                                                                   flat=True)
    if district not in districts and district not in ["Ro'yxatda yo'q", "Нет в списке"]:
        if user.lang == 'ru':
            text = 'Вы ввели некорректный район. Попробуйте еще раз'
        else:
            text = "👇🏻 *Mahallangizni tanalang*:\n\n❗️quyidagi tugmalardan foydalaning"

        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            parse_mode='Markdown'
        )
        return states.GET_DISTRICT

    save_data_to_cache(update, district, request_name='district')
    send_saved_message_text(user, bot, update)
    return admission.get_problem_type(bot, update)
