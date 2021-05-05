# Generated by Django 3.2 on 2021-05-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0036_alter_murojatchi_year_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='murojatchi',
            name='day_of_birth',
            field=models.PositiveIntegerField(blank=True, max_length=256, null=True, verbose_name="Tug'ilgan kun"),
        ),
        migrations.AlterField(
            model_name='murojatchi',
            name='month_of_birth',
            field=models.PositiveIntegerField(blank=True, max_length=256, null=True, verbose_name="Tug'ilgan oy"),
        ),
    ]