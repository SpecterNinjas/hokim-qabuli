from django.db import models
from telegram import Bot

from hokim_qabuli import settings


class TelegramProfile(models.Model):
    external_id = models.PositiveIntegerField()
    username = models.CharField(max_length=255)
    lang = models.CharField(max_length=255)


class Text(models.Model):
    text_id = models.CharField(primary_key=True, unique=True, max_length=255)
    buttons_uz = models.CharField(max_length=700, blank=True, null=True)
    buttons_ru = models.CharField(max_length=700, blank=True, null=True)
    uz = models.TextField()
    ru = models.TextField()

    def __str__(self):
        return f'{self.text_id}{self.buttons_ru}{self.buttons_uz}'
    

class Month(models.Model):
    title = models.CharField(max_length=255, null=True)
    title_uz = models.CharField(max_length=255, null=True)
    title_ru = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.title}'


class District(models.Model):
    region = models.CharField(verbose_name='Tuman', max_length=255, null=True)
    title_uz = models.CharField(max_length=255, null=True)
    title_ru = models.CharField(max_length=255, null=True)
    token = models.CharField(max_length=1024, null=True)

    def __str__(self):
        return f'{self.title_uz}'

    class Meta:
        verbose_name = 'Махаля'
        verbose_name_plural = 'Махали'


class Admission(models.Model):
    external_id = models.CharField(max_length=255, null=True)
    request_type = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    problem_type = models.CharField(max_length=255, null=True)
    sub_problem = models.CharField(max_length=255, null=True)
    short_description = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=13, null=True)

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = 'Qabul'
        verbose_name_plural = 'Qabullar'


class RegionBot(models.Model):
    title = models.CharField(verbose_name='Bot nomi', max_length=1024, null=True)
    region = models.CharField(verbose_name='Tuman', max_length=1024, null=True)
    district = models.CharField(verbose_name='Mahalla', max_length=1024, null=True)
    token = models.CharField(max_length=1024, null=True)

    def save(self, *args, **kwargs):
        bot = Bot(str(self.token))
        bot.set_webhook(self.webhook_url)

        super().save(*args, **kwargs)

    @property
    def webhook_url(self):
        return f"{settings.HOST}/bot/{self.token}/"

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Bot'
        verbose_name_plural = 'Botlar'
