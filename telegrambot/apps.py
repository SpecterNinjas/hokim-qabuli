from django.apps import AppConfig, apps
import logging

text_manager = apps.get_model('telegrambot', 'Text')


def log_errors(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logging.exception(e)

    return inner


class TelegrambotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegrambot'
