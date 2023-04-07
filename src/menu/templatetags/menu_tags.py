from django import template
from ..models import Menu


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(request):
    menu_items = Menu.objects.filter(parent=None)
    return _render_menu(menu_items, request)


def _render_menu(menu_items, current_path):
    menu_html = '<menu>'
    for item in menu_items:
        submenu_html = _render_menu(item.children.all(), current_path) if item.children.exists() else ''
        menu_html += f'<menuitem><a href="{item.url}">{item.name}</a>{submenu_html}</menuitem>'
    menu_html += '</menu>'
    return menu_html
