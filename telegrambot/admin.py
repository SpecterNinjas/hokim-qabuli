from django.contrib import admin

# Register your models here.
from telegrambot.models import TelegramProfile, Text, District, Admission, RegionBot, Month


@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'username', 'lang')


@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_uz', 'title_ru')


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('text_id', 'buttons_uz', 'buttons_ru', 'uz', 'ru')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('region', 'title_uz', 'title_ru', 'token')


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = (
        'external_id', 'request_type', 'first_name', 'middle_name', 'last_name', 'district', 'problem_type',
        'sub_problem',
        'short_description', 'phone_number')


@admin.register(RegionBot)
class RegionBotAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'district', 'token')
