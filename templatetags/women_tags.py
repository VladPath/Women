from django import template
from women import views

register = template.Library()

@register.simple_tag()
def get_catigories():
    return views.cats_db

@register.inclusion_tag('women/list_catigories.html')
def show_catigories(cat_selected=0):
    cats = views.cats_db
    return {'cats':cats, 'cat_selected': cat_selected }
