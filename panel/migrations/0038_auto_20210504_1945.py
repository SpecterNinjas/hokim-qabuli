# Generated by Django 3.2 on 2021-05-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0037_auto_20210504_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='murojatchi',
            name='day_of_birth',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name="Tug'ilgan kun"),
        ),
        migrations.AlterField(
            model_name='murojatchi',
            name='month_of_birth',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name="Tug'ilgan oy"),
        ),
    ]
