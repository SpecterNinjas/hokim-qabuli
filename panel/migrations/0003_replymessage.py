# Generated by Django 3.2 on 2021-04-29 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_alter_murojatchi_telegram_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReplyMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Javob Matni')),
                ('updated', models.DateField(auto_now=True, verbose_name="Oxirgi O'zgartirish Kiritilgan Sana")),
                ('telegram_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.murojatchi')),
            ],
            options={
                'verbose_name': 'Javob Matni',
                'verbose_name_plural': 'Javob Matnlari',
            },
        ),
    ]