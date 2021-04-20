import json
import logging
from django.conf import settings
from telegram import Bot, Update
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telegram.ext import Dispatcher

from telegrambot.main import conv_handler

logger = logging.getLogger(__name__)

bot = Bot(settings.TELEGRAM_TOKEN)
bot.set_webhook(f'{settings.HOST}/bot/')


@csrf_exempt
def webhook(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        update = Update.de_json(data, bot)
        dispatcher = Dispatcher(bot, None, workers=0, use_context=False)
        dispatcher.add_handler(conv_handler)
        dispatcher.process_update(update)
    except Exception as e:
        logger.exception(e)
        logger.warning(f'Telegram bot receive invalid request : {repr(request)}')
        return JsonResponse({})

    return JsonResponse({})
