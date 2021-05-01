from django import template
from modeltranslation.utils import get_language

register = template.Library()


@register.simple_tag(name='get_language_url')
def get_language_url(request, lang):
    active_language = get_language()
    return request.get_full_path().replace(active_language, lang, 1)
