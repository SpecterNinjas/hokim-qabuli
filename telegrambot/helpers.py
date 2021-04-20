from telegram import InlineKeyboardButton


def get_request_data(
        telegram_id=None,
        first_name=None,
        last_name=None,
        middle_name=None,
        district=None,
        problem_type=None,
        sub_problem=None,
        short_description=None,
):
    request = {
        'telegram_id': telegram_id,
        'first_name': first_name,
        'last_name': last_name,
        'middle_name': middle_name,
        'district': district,
        'problem_type': problem_type,
        'sub_problem': sub_problem,
        'short_description': short_description,
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
