from django import template
from women import views
from women.models import Category

register = template.Library()


@register.inclusion_tag('women/list_catigories.html')
def show_catigories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats':cats, 'cat_selected': cat_selected }
