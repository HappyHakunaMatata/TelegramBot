from django import template

register = template.Library()

@register.simple_tag
def form_type(parameter):
    return parameter

