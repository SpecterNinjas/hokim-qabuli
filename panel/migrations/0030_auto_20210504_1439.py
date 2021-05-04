# Generated by Django 3.2 on 2021-05-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0029_alter_murojatchi_murojat_turi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='murojatchi',
            name='murojat_turi',
            field=models.CharField(blank=True, choices=[('Appeal', 'Murojat'), ('Admission', 'Qabul')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='murojatchi',
            name='status',
            field=models.CharField(blank=True, choices=[("ko'rib chiqilmagan", "ko'rib chiqilmagan"), ("ko'rib chiqilmoqda", "ko'rib chiqilmoqda"), ("ko'rib chiqildi", "ko'rib chiqildi"), ('rad etildi', 'rad etildi')], default="ko'rib chiqilmagan", max_length=32, null=True, verbose_name='Murojatchi Statusi'),
        ),
    ]
