from django.shortcuts import render
from .templatetags.menu_tags import draw_menu


def render_menu_view(request):
    rendered_menu = draw_menu(request.path)
    return render(request, 'menu/base.html', {'menu_items': rendered_menu})
