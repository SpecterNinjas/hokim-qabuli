# Generated by Django 3.2 on 2021-04-29 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_alter_murojatchi_murojat_turi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='murojatchi',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.submuammo'),
        ),
        migrations.AlterField(
            model_name='murojatchi',
            name='muammo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.muammo'),
        ),
        migrations.AlterField(
            model_name='murojatchi',
            name='status',
            field=models.CharField(choices=[("ko'rib chiqilmagan", "ko'rib chiqilmagan"), ("ko'rib chiqilmoqda", "ko'rib chiqilmoqda"), ("ko'rib chiqildi", "ko'rib chiqildi"), ('qabulga chaqirildi', 'qabulga chaqirildi'), ('rad etildi', 'rad etildi')], default="ko'rib chiqilmagan", max_length=32, verbose_name='Murojatchi Statusi'),
        ),
    ]