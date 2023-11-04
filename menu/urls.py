from django.urls import path
from .views import menu_items_view

urlpatterns = [
    path('', menu_items_view, name="item-detail"),
    path('<int:pk>/', menu_items_view, name="item-detail"),
]
