from django.urls import path

from apps.customers.api.api import customers_api_view, customer_detail_view, get_balance_view

urlpatterns = [
    path('customer/', customers_api_view, name='Customer'),
    path('customer/<str:pk>/', customer_detail_view, name='Customer detail'),
    path('balance/<str:pk>/', get_balance_view, name='Balance'),
]