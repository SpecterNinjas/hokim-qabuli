# Generated by Django 3.2 on 2021-05-03 08:14
import json
import os

from django.db import migrations

from hokim_qabuli.settings import BASE_DIR
from telegrambot.models import Month


def load_month(apps, scheme_editor):
    with open(os.path.join(BASE_DIR, 'common_month.json'), encoding='utf8', errors='ignore') as json_file:
        data = json.load(json_file)
        for month in data:
            Month.objects.create(
                title=month['title'],
                title_uz=month['title_uz'],
                title_ru=month['title_ru'],
            )


def reverse_func(apps, scheme_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('telegrambot', '0003_month'),
    ]

    operations = [
        migrations.RunPython(load_month, reverse_func)
    ]
