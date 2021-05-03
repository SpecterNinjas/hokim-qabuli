from .models import *
from modeltranslation.translator import register, TranslationOptions


@register(Mahalla)
class MahallaTranslationOptions(TranslationOptions):
    fields = ['location']


@register(Muammo)
class MuammoTranslationOptions(TranslationOptions):
    fields = ['title', ]


@register(SubMuammo)
class SubMuammoTranslationOptions(TranslationOptions):
    fields = ['category', ]


@register(Hudud)
class HududTranslationOptions(TranslationOptions):
    fields = ['title', ]


@register(Murojatchi)
class MurojatchiTranslationOptions(TranslationOptions):
    fields = ['location', 'description']
