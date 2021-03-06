# Generated by Django 3.2 on 2021-05-05 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hudud',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, verbose_name='Hudud')),
                ('title_uz', models.CharField(max_length=128, null=True, verbose_name='Hudud')),
                ('title_ru', models.CharField(max_length=128, null=True, verbose_name='Hudud')),
            ],
            options={
                'verbose_name': 'Hudud',
                'verbose_name_plural': 'Hudud',
            },
        ),
        migrations.CreateModel(
            name='Mahalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, null=True, verbose_name='Mahalla nomi')),
                ('region', models.CharField(max_length=255, null=True, verbose_name='Tuman')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='Mahalla nomi_ru')),
                ('title_uz', models.CharField(max_length=256, null=True, verbose_name='Mahalla nomi_uz')),
                ('token', models.CharField(max_length=1024, null=True)),
                ('location', models.CharField(max_length=256, null=True, verbose_name='Manzil')),
                ('location_uz', models.CharField(max_length=256, null=True, verbose_name='Manzil')),
                ('location_ru', models.CharField(max_length=256, null=True, verbose_name='Manzil')),
                ('phone', models.CharField(max_length=13, null=True, verbose_name='Telefon')),
            ],
            options={
                'verbose_name': 'Mahalla',
                'verbose_name_plural': 'Mahallalar',
            },
        ),
        migrations.CreateModel(
            name='Muammo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Muammo nomi')),
                ('title_uz', models.CharField(max_length=300, null=True, verbose_name='Muammo nomi')),
                ('title_ru', models.CharField(max_length=300, null=True, verbose_name='Muammo nomi')),
            ],
            options={
                'verbose_name': 'Muammo nomi',
                'verbose_name_plural': 'Muammolar',
            },
        ),
        migrations.CreateModel(
            name='Murojatchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Telegram ID')),
                ('fullname', models.CharField(blank=True, max_length=256, null=True, verbose_name='Ism Sharifi')),
                ('username', models.CharField(blank=True, max_length=32, null=True, verbose_name='Username')),
                ('murojat_turi', models.CharField(blank=True, choices=[('appeal', 'Murojat'), ('admission', 'Qabul')], max_length=16, null=True)),
                ('media', models.FileField(blank=True, null=True, upload_to='muammo_media/', verbose_name='Media')),
                ('location', models.CharField(blank=True, max_length=300, null=True, verbose_name='Manzil')),
                ('location_uz', models.CharField(blank=True, max_length=300, null=True, verbose_name='Manzil')),
                ('location_ru', models.CharField(blank=True, max_length=300, null=True, verbose_name='Manzil')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Murojat Matni')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefon')),
                ('reply_message', models.TextField(blank=True, default='Javob berilmagan', null=True, verbose_name='Javob Matni')),
                ('created', models.DateField(auto_now_add=True, null=True, verbose_name='Murojat Sanasi')),
                ('updated', models.DateField(auto_now_add=True, null=True, verbose_name="O'zgartish Kiritilgan Sana")),
                ('status', models.CharField(blank=True, choices=[("ko'rib chiqilmagan", "ko'rib chiqilmagan"), ("ko'rib chiqilmoqda", "ko'rib chiqilmoqda"), ("ko'rib chiqildi", "ko'rib chiqildi"), ('rad etildi', 'rad etildi')], default="ko'rib chiqilmagan", max_length=32, null=True, verbose_name='Murojatchi Statusi')),
                ('year_of_birth', models.PositiveIntegerField(blank=True, null=True, verbose_name="Tug'ilgan yil")),
                ('month_of_birth', models.CharField(blank=True, max_length=256, null=True, verbose_name="Tug'ilgan oy")),
                ('day_of_birth', models.CharField(blank=True, max_length=256, null=True, verbose_name="Tug'ilgan kun")),
                ('gender', models.PositiveBigIntegerField(blank=True, choices=[(1, 'Erkak'), (2, 'Ayol')], null=True, verbose_name='Gender')),
            ],
            options={
                'verbose_name': 'Murojatchi',
                'verbose_name_plural': 'Murojatchilar',
            },
        ),
        migrations.CreateModel(
            name='ProfileSuggestion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('telegram_id', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Telegram ID')),
                ('fullname', models.CharField(blank=True, max_length=256, null=True, verbose_name='Ism Sharifi')),
                ('phone', models.CharField(blank=True, max_length=13, null=True, verbose_name='Telefon')),
                ('year_of_birth', models.CharField(blank=True, max_length=256, null=True, verbose_name="Tug'ilgan yil")),
                ('month_of_birth', models.CharField(blank=True, max_length=256, null=True, verbose_name="Tug'ilgan oy")),
                ('day_of_birth', models.CharField(blank=True, max_length=256, null=True, verbose_name="Tug'ilgan kun")),
                ('gender', models.PositiveBigIntegerField(blank=True, choices=[(1, 'Erkak'), (2, 'Ayol')], null=True, verbose_name='Gender')),
            ],
        ),
        migrations.CreateModel(
            name='SubMuammo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='Default', max_length=64, verbose_name='Kategoriya')),
                ('category_uz', models.CharField(default='Default', max_length=64, null=True, verbose_name='Kategoriya')),
                ('category_ru', models.CharField(default='Default', max_length=64, null=True, verbose_name='Kategoriya')),
                ('title', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='panel.muammo')),
            ],
            options={
                'verbose_name': 'Kategoriya nomi',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Qabul Nomi')),
                ('appointment', models.DateField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('status', models.IntegerField(blank=True, choices=[(1, "Ko'rib Chiqildi"), (2, "Ko'rib Chiqilmoqda"), (3, "Ko'rib Chiqilmagan")], default=3, null=True)),
                ('users', models.ManyToManyField(blank=True, to='panel.Murojatchi')),
            ],
            options={
                'verbose_name': 'Qabul',
                'verbose_name_plural': 'Qabullar',
            },
        ),
        migrations.AddField(
            model_name='murojatchi',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.submuammo'),
        ),
        migrations.AddField(
            model_name='murojatchi',
            name='hudud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.hudud'),
        ),
        migrations.AddField(
            model_name='murojatchi',
            name='mahalla',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.mahalla'),
        ),
        migrations.AddField(
            model_name='murojatchi',
            name='muammo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.muammo'),
        ),
    ]
