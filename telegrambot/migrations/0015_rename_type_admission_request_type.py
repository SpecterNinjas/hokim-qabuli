# Generated by Django 3.2 on 2021-04-29 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegrambot', '0014_admission_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='type',
            new_name='request_type',
        ),
    ]
