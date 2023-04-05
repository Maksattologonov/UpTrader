from django import template
from django.shortcuts import render

from .models import Menu


register = template.Library()


@register.simple_tag()
def draw_menu(request, menu_name):
    menu_items = Menu.objects.filter(parent=None, url=menu_name)
    context = {
        "menu": menu_items
    }
    return render(request, 'menu/base.html', context)


# def _render_menu(menu_items, current_path):
#     menu_html = '<ul>'
#     for item in menu_items:
#         is_active = current_path.startswith(item.url) if item.url else False
#         submenu_html = _render_menu(item.children.all(), current_path) if item.children.exists() else ''
#         active_class = 'active' if is_active else ''
#         menu_html += f'<li class="{active_class}"><a href="{item.url}">{item.name}</a>{submenu_html}</li>'
#     menu_html += '</ul>'
#     return menu_html
