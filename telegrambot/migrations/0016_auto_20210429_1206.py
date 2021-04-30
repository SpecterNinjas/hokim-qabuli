# Generated by Django 3.2 on 2021-04-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegrambot', '0015_rename_type_admission_request_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionbot',
            name='district',
            field=models.CharField(max_length=1024, null=True, verbose_name='Mahalla'),
        ),
        migrations.AlterField(
            model_name='regionbot',
            name='region',
            field=models.CharField(max_length=1024, null=True, verbose_name='Tuman'),
        ),
        migrations.AlterField(
            model_name='regionbot',
            name='title',
            field=models.CharField(max_length=1024, null=True, verbose_name='Bot nomi'),
        ),
    ]
