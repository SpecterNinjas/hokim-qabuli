from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


@admin.register(Mahalla)
class MahallaAdmin(TranslationAdmin):
    list_display = ['title', 'location', 'phone']
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
    list_display = ['telegram_id', 'username', 'fullname', 'hudud', 'mahalla', 'muammo', 'category', 'phone','reply_message', 'created',
                    'status']
    search_fields = ['fullname', ]


# @admin.register(ReplyMessage)
# class ReplyMessageAdmin(admin.ModelAdmin):
#     list_display = ['telegram_id', 'updated']
#     search_fields = ['telegram_id', ]



    # def render_change_form(self, request, context, *args, **kwargs):
    #
    #     print("Before:",context['adminform'].form.fields['muammo'])
    #     context['adminform'].form.fields['category'].queryset = SubMuammo.objects.filter(category__icontains='suv')
    #
    #     return super(MurojatchiAdmin, self).render_change_form(request, context, *args, **kwargs)

