from django import template

from ..models import *

register = template.Library()


@register.simple_tag()
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = Menu.objects.filter(parent=None, url=menu_name)
    return _render_menu(menu_items, request.path)


def _render_menu(menu_items, current_path):
    menu_html = '<ul> HELLO'
    for item in menu_items:
        is_active = current_path.startswith(item.url) if item.url else False
        submenu_html = _render_menu(item.children.all(), current_path) if item.children.exists() else ''
        active_class = 'active' if is_active else ''
        menu_html += f'<li class="{active_class}"><a href="{item.url}">{item.name}</a>{submenu_html}</li>'
    menu_html += '</ul>'
    return menu_html
