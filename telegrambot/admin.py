from django.contrib import admin

# Register your models here.
from telegrambot.models import TelegramProfile, Text


@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'username', 'lang')


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('text_id', 'buttons_uz', 'buttons_ru', 'uz', 'ru')
