from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.render_menu_view, name='render_menu')
]
