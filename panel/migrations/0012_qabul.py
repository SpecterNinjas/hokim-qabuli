# Generated by Django 3.2 on 2021-05-01 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_murojatchi_accepted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qabul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Qabul Nomi')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Yaratildi')),
                ('updated', models.DateField(auto_now=True, verbose_name="O'zgartirildi")),
                ('fullname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.murojatchi')),
            ],
            options={
                'verbose_name': 'Qabul',
                'verbose_name_plural': 'Qabullar',
            },
        ),
    ]
