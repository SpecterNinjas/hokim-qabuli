import json
import logging
from django.conf import settings
from telegram import Bot, Update
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram.ext import Dispatcher

from telegrambot.apps import log_errors
from telegrambot.main import conv_handler
from telegrambot.models import RegionBot

logger = logging.getLogger(__name__)

# bot = Bot(settings.TELEGRAM_TOKEN)
# bot.set_webhook(f'{settings.HOST}/bot/{settings.TELEGRAM_TOKEN}/')


@csrf_exempt
def webhook(request, token):
    _token = RegionBot.objects.filter(token=token).last()
    bot = Bot(_token.token)
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
