from django.db import models


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

# class Admission(models.Model):
#     external_id = models.CharField(max_length=255, null=True)
#     first_name = models.CharField(max_length=255, null=True)
#     middle_name = models.CharField(max_length=255, null=True)
#     last_name = models.CharField(max_length=255, null=True)
