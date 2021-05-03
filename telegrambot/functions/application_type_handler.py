import re
from django.core.cache import cache
from telegram import Bot, Update


def application_type_handler(bot: Bot, update: Update):
    print('application_type_handler')
    print(update.message.text)
    request_type = update.message.text
    request = cache.get(f'request_{update.effective_chat.id}')
    # if re.match()