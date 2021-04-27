from django.contrib import admin

from .models import Mahalla, Muammo, Murojatchi, SubMuammo


@admin.register(Mahalla)
class MahallaAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'phone']
    search_fields = ['location', 'title']


@admin.register(Muammo)
class MuammoAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ['title', ]


@admin.register(SubMuammo)
class SubMuammoAdmin(admin.ModelAdmin):
    list_display = ['category', ]
    search_fields = ['category', ]


@admin.register(Murojatchi)
class MurojatchiAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'mahalla', 'muammo', 'category', 'phone', 'created', 'status']
    search_fields = ['fullname', ]

    # def render_change_form(self, request, context, *args, **kwargs):
    #
    #     print("Before:",context['adminform'].form.fields['muammo'])
    #     context['adminform'].form.fields['category'].queryset = SubMuammo.objects.filter(category__icontains='suv')
    #
    #     return super(MurojatchiAdmin, self).render_change_form(request, context, *args, **kwargs)