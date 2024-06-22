# store/urls.py

from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<str:category_name>/', views.product_list_by_category, name='category'),
    path('<str:category_name>/<int:id>/', views.product_detail, name='product_detail'),
]
