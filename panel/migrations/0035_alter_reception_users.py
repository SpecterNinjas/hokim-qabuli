# Generated by Django 3.2 on 2021-05-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0034_auto_20210504_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reception',
            name='users',
            field=models.ManyToManyField(blank=True, to='panel.Murojatchi'),
        ),
    ]