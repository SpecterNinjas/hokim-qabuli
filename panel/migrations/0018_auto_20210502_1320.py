# Generated by Django 3.2 on 2021-05-02 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0017_delete_qabul'),
    ]

    operations = [
        migrations.AlterField(
            model_name='murojatchi',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.submuammo'),
        ),
        migrations.AlterField(
            model_name='murojatchi',
            name='hudud',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.hudud'),
        ),
        migrations.AlterField(
            model_name='murojatchi',
            name='murojat_turi',
            field=models.CharField(blank=True, choices=[('Taklif', 'Taklif'), ('Murojat', 'Murojat'), ('Qabul', 'Qabul')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='murojatchi',
            name='reply_message',
            field=models.TextField(blank=True, default='Javob berilmagan', null=True, verbose_name='Javob Matni'),
        ),
    ]
