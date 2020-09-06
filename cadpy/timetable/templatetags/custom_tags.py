from django import template

register = template.Library()


@register.simple_tag
def increment(a):
    return (a+1)
