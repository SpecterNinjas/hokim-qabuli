# Generated by Django 3.2 on 2021-04-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='murojatchi',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]