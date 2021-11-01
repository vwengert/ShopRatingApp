"""Defines URL patterns for rating_app"""

from django.urls import path
from . import views

app_name = 'rating_app'
urlpatterns = [
    # Startseite
    path('', views.index, name='index'),
    path('shops/', views.shops, name='shops'),
    path('shops/<int:shop_id>/', views.shop, name="shop"),
    path('new_shop/', views.new_shop, name='new_shop'),
    path('new_rating/<int:shop_id>/', views.new_rating, name='new_rating'),
    path('edit_rating/<int:rating_id>/', views.edit_rating, name='edit_rating'),
]