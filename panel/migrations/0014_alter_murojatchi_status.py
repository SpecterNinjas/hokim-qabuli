# Generated by Django 3.2 on 2021-05-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0013_auto_20210502_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='murojatchi',
            name='status',
            field=models.CharField(blank=True, choices=[("ko'rib chiqilmagan", "ko'rib chiqilmagan"), ("ko'rib chiqilmoqda", "ko'rib chiqilmoqda"), ("ko'rib chiqildi", "ko'rib chiqildi"), ('qabulga chaqirildi', 'qabulga chaqirildi'), ('rad etildi', 'rad etildi')], default="ko'rib chiqilmagan", max_length=32, null=True, verbose_name='Murojatchi Statusi'),
        ),
    ]
