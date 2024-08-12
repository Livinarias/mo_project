from django.urls import path

from apps.loans.api.api import create_loans_api_view, get_loan_by_customer_view

urlpatterns = [
    path('loan/', create_loans_api_view, name='Loan'),
    path('loan/<str:pk>/', get_loan_by_customer_view, name='Loan detail'),
]