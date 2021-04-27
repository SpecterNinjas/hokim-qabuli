import datetime
import re

from django import template
from django.core.serializers import serialize
from django.utils.timezone import now
from modeltranslation.utils import get_language

# from panel.models.territorial import Region
import json
from django.core.serializers.json import DjangoJSONEncoder

register = template.Library()


@register.simple_tag(name='get_language_url')
def get_language_url(request, lang):
    active_language = get_language()
    return request.get_full_path().replace(active_language, lang, 1)


@register.filter
def json(queryset):
    return serialize('json', queryset)

# @register.filter
# def json(queryset):
#     structure = json.dumps(queryset)
#     return structure
