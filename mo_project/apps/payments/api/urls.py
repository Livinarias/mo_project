from django.urls import path

from apps.payments.api.api import create_payments_api_view, get_payment_by_customer_view

urlpatterns = [
    path('payment/', create_payments_api_view, name='payment'),
    path('payment/<str:pk>/', get_payment_by_customer_view, name='Payment detail'),
]