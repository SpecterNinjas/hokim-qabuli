from django.apps import apps
from django.core.cache import cache
from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton

from telegrambot import states
from telegrambot.apps import log_errors
from telegrambot.helpers import get_request_data, generate_inline_keyboard, validate_admission_info
from telegrambot.models import Text


@log_errors
def main_menu(bot: Bot, update: Update):
    print('main_menu')

    user_model = apps.get_model('telegrambot', 'TelegramProfile')
    user = user_model.objects.get(external_id=update.effective_chat.id)
    try:
        if update.callback_query.data != 'back_to_admission_menu':
            request_type = update.callback_query.data
    except:
        pass

    if cache.get(f'request_{update.effective_chat.id}') is None:
        request = get_request_data()
        cache.set(f'request_{update.effective_chat.id}', request)
    else:
        request = cache.get(f'request_{update.effective_chat.id}')
        try:
            if update.callback_query.data != 'back_to_admission_menu':
                request['request_type'] = request_type
                cache.set(f'request_{update.effective_chat.id}', request)
        except:
            pass
    no_data = {
        'uz': "Ma'lumot yoq",
        'ru': "Нет данных",
    }

    first_name_sign = '✅️ ' if request['first_name'] else '❗️'
    first_name = request['first_name'] if request['first_name'] else no_data[user.lang]

    last_name_sign = '✅️ ' if request['last_name'] else '❗️'
    last_name = request['last_name'] if request['last_name'] else no_data[user.lang]

    middle_name_sign = '✅️ ' if request['middle_name'] else '❗️'
    middle_name = request['middle_name'] if request['middle_name'] else no_data[user.lang]

    date_of_birth_sign = '✅️ ' if request['date_of_birth'] else '❗️'
    date_of_birth = request['date_of_birth'] if request['date_of_birth'] else no_data[user.lang]

    gender_sign = '✅️ ' if request['gender'] else '❗️'
    gender = request['gender'] if request['gender'] else no_data[user.lang]

    district_sign = '✅️ ' if request['district'] else '❗️'
    district = request['district'] if request['district'] else no_data[user.lang]

    problem_type_sign = '✅️ ' if request['problem_type'] else '❗️'
    problem_type = request['problem_type'] if request['problem_type'] else no_data[user.lang]

    sub_problem_sign = '✅️ ' if request['sub_problem'] else '❗️'
    sub_problem = request['sub_problem'] if request['sub_problem'] else no_data[user.lang]

    short_description_sign = '✅️ ' if request['short_description'] else '❗️'
    short_description = request['short_description'] if request['short_description'] else no_data[user.lang]

    if request['request_type'] == 'appeal' or request['request_type'] == 'offer':
        file_sign = '✅️ ' if request['file'] else '❗️'
        file = request['file'] if request['file'] else no_data[user.lang]

        location_sign = '✅️ ' if request['location'] else '❗️'
        location = request['location'] if request['location'] else no_data[user.lang]

    phone_number_sign = '✅️ ' if request['phone_number'] else '❗️'
    phone_number = request['phone_number'] if request['phone_number'] else no_data[user.lang]

    if request['request_type'] == 'appeal' or request['request_type'] == 'offer':
        data = Text.objects.filter(text_id='APPEAL_MENU').values()[0]
    else:
        data = Text.objects.filter(text_id='ADMISSION_MENU').values()[0]

    if request['request_type'] == 'appeal' or request['request_type'] == 'offer':
        text = data[user.lang].format(
            first_name_sign=first_name_sign, first_name=first_name,
            middle_name_sign=middle_name_sign, middle_name=middle_name,
            last_name_sign=last_name_sign, last_name=last_name,
            date_of_birth_sign=date_of_birth_sign, date_of_birth=date_of_birth,
            gender_sign=gender_sign, gender=gender,

            district_sign=district_sign, district=district,
            problem_type_sign=problem_type_sign, problem_type=problem_type,
            sub_problem_sign=sub_problem_sign, sub_problem=sub_problem,
            short_description_sign=short_description_sign, short_description=short_description,
            file_sign=file_sign, file=file,

            location_sign=location_sign, location=location,
            phone_number_sign=phone_number_sign, phone_number=phone_number,
        )
    else:
        text = data[user.lang].format(
            first_name_sign=first_name_sign, first_name=first_name,
            middle_name_sign=middle_name_sign, middle_name=middle_name,
            last_name_sign=last_name_sign, last_name=last_name,
            date_of_birth_sign=date_of_birth_sign, date_of_birth=date_of_birth,
            gender_sign=gender_sign, gender=gender,

            district_sign=district_sign, district=district,
            problem_type_sign=problem_type_sign, problem_type=problem_type,
            sub_problem_sign=sub_problem_sign, sub_problem=sub_problem,
            short_description_sign=short_description_sign, short_description=short_description,
            phone_number_sign=phone_number_sign, phone_number=phone_number,
        )

    inline_keyboard = generate_inline_keyboard(data[f"buttons_{user.lang}"], update.effective_chat.id)

    if validate_admission_info(request):
        save_btn_text = "✉️Saqlash" if user.lang == 'uz' else '✉️Сохранить'
        back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'
        inline_keyboard.append(
            [
                InlineKeyboardButton(back_btn_text, callback_data='back_to_statement_type'),
                InlineKeyboardButton(save_btn_text, callback_data='save_admission_info'),
            ],
        )
    else:
        back_btn_text = "⬅️️Orqaga" if user.lang == 'uz' else '⬅️ Назад'
        inline_keyboard.append(
            [InlineKeyboardButton(back_btn_text, callback_data='back_to_statement_type')]
        )

    try:
        bot.edit_message_text(
            chat_id=update.effective_chat.id,
            text=text,
            message_id=update.callback_query.message.message_id,
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
            parse_mode='HTML'
        )
    except:
        bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            reply_markup=InlineKeyboardMarkup(inline_keyboard),
            parse_mode='HTML',
        )
    return states.MAIN