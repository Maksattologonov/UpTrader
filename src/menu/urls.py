from django.urls import path
from . import views

urlpatterns = [
    path("<str:menu_name>", views.draw_menu, name='menu_name'),
]
