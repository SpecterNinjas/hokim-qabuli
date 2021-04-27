import json
import os

from django.db import migrations

from hokim_qabuli.settings import BASE_DIR
from telegrambot.models import Text


def load_text_template(apps, scheme_editor):
    with open(os.path.join(BASE_DIR, 'text_template.json'), encoding='utf8', errors='ignore') as json_file:
        data = json.load(json_file)
        for item in data:
            Text.objects.create(
                text_id=item['pk'],
                buttons_uz=item['fields']['buttons_uz'],
                buttons_ru=item['fields']['buttons_ru'],
                uz=item['fields']['uz'],
                ru=item['fields']['ru'],
            )


def reverse_func(apps, scheme_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('telegrambot', '0007_auto_20210421_0915'),
    ]

    operations = [
        migrations.RunPython(load_text_template, reverse_func)
    ]
