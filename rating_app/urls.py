"""Defines URL patterns for rating_app"""

from django.urls import path
from . import views

app_name = 'rating_app'
urlpatterns = [
    # Startseite
    path('', views.index, name='index'),
    path('shops/', views.shops, name='shops'),
    path('shops/<int:shop_id>/', views.shop, name="shop")
]