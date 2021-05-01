from django.contrib import admin

from .models import *


@admin.register(Mahalla)
class MahallaAdmin(admin.ModelAdmin):
    list_display = ['title', 'region', 'title_uz', 'title_ru', 'token', 'location', 'phone', ]
    search_fields = ['location', 'title']


@admin.register(Muammo)
class MuammoAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ['title', ]


@admin.register(Hudud)
class HududAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ['title', ]


@admin.register(SubMuammo)
class SubMuammoAdmin(admin.ModelAdmin):
    list_display = ['category', ]
    search_fields = ['category', ]


@admin.register(Murojatchi)
class MurojatchiAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'username', 'fullname', 'last_name', 'middle_name', 'year_of_birth',
                    'month_of_birth', 'day_of_birth', 'gender', 'hudud', 'mahalla', 'muammo', 'category', 'phone',
                    'description', 'reply_message', 'created', 'status']
    search_fields = ['fullname', ]
