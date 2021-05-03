from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


@admin.register(Mahalla)
class MahallaAdmin(TranslationAdmin):
    list_display = ['title', 'region', 'location', 'phone']
    search_fields = ['location', 'title']


@admin.register(Muammo)
class MuammoAdmin(TranslationAdmin):
    list_display = ['title', ]
    search_fields = ['title', ]


@admin.register(Hudud)
class HududAdmin(TranslationAdmin):
    list_display = ['title', ]
    search_fields = ['title', ]


@admin.register(SubMuammo)
class SubMuammoAdmin(TranslationAdmin):
    list_display = ['category', ]
    search_fields = ['category', ]


@admin.register(Murojatchi)
<<<<<<< HEAD
class MurojatchiAdmin(TranslationAdmin):
    list_display = ['telegram_id', 'username', 'fullname', 'hudud', 'mahalla', 'muammo', 'category', 'phone',
                    'reply_message', 'created',
                    'status']

=======
class MurojatchiAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'username', 'fullname', 'year_of_birth',
                    'month_of_birth', 'day_of_birth', 'gender', 'hudud', 'mahalla', 'muammo', 'category', 'phone',
                    'description', 'reply_message', 'created', 'status']
>>>>>>> e9dd7abd78320142ff2340b3dbeb4ea79aecd580
    search_fields = ['fullname', ]


@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'appointment', 'created', 'updated']
    search_fields = ['title', ]
