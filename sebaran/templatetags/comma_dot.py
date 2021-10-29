from django import template

register = template.Library()

@register.filter
def comma_dot(value):
    return value.replace(",", ".")
