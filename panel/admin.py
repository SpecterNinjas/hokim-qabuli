from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


@admin.register(Mahalla)
class MahallaAdmin(TranslationAdmin):
    list_display = ['id','title', 'region', 'location', 'phone']
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
class MurojatchiAdmin(TranslationAdmin):
    list_display = ['fullname', 'hudud', 'mahalla', 'muammo', 'category', 'phone',
                    'reply_message', 'created',
                    'status']

    search_fields = ['fullname', ]


@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'appointment', 'created', 'status']
    search_fields = ['title', ]
