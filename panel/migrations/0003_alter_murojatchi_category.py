# Generated by Django 3.2 on 2021-04-23 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_alter_murojatchi_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='murojatchi',
            name='category',
            field=models.ForeignKey(blank=True, default='Boshqa', null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.submuammo'),
        ),
    ]
