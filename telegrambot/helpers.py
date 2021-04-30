from telegram import InlineKeyboardButton


def get_request_data(
        telegram_id=None,
        request_type=None,
        first_name=None,
        last_name=None,
        middle_name=None,

        year_of_birth=None,
        month_of_birth=None,
        day_of_birth=None,
        gender=None,
        district=None,

        problem_type=None,
        sub_problem=None,
        short_description=None,
        problem_address=None,
        media=None,
        location=None,
        phone_number=None,
):
    request = {
        'telegram_id': telegram_id,
        'request_type': request_type,
        'first_name': first_name,
        'last_name': last_name,
        'middle_name': middle_name,

        'year_of_birth': year_of_birth,
        'month_of_birth': month_of_birth,
        'day_of_birth': day_of_birth,
        'gender': gender,
        'district': district,

        'problem_type': problem_type,
        'sub_problem': sub_problem,
        'short_description': short_description,
        'problem_address': problem_address,
        'media': media,
        'location': location,
        'phone_number': phone_number,
    }

    return request


def _generate_inline_rows(rows):
    x = [rows[i:i + 2] for i in range(0, len(rows), 2)]
    return x


def generate_inline_keyboard(data, chat_id=None):
    keyboard = []
    rows = data.splitlines()
    for row in rows:
        keyboard_rows = []
        buttons = row.split("|")
        for button in buttons:
            text, callback_data = button.strip().split(">")
            keyboard_rows.append(InlineKeyboardButton(text.strip(), callback_data=callback_data.strip()))
        keyboard.append(keyboard_rows)
        keyboard = _generate_inline_rows(keyboard[0])
    return keyboard


def validate_admission_info(request):
    if (request['telegram_id'] and
            request['first_name'] and
            request['last_name'] and
            request['middle_name'] and
            request['year_of_birth'] and
            request['month_of_birth'] and
            request['day_of_birth'] and
            request['gender'] and

            request['district'] and
            request['problem_type'] and
            request['sub_problem'] and
            request['short_description'] and
            request['phone_number']):
        return True
    return False
