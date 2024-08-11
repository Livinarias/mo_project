from django.contrib import admin

from apps.payments.models import Payments, PaymentsDetails


class AdminPayments(admin.ModelAdmin):
    list_display = [
        'created_at', 
        'external_id',
        'total_amount',
        'status',  
        'paid_at',
        'customer_id'
    ]
    list_filter = [
        'external_id',
        'status',
        'total_amount',
        'customer_id'
    ]
    search_fields = ['external_id', 'status', 'total_amount', 'customer_id']
    class Meta:
        model = Payments

admin.site.register(Payments, AdminPayments)


class AdminPaymentDetails(admin.ModelAdmin):
    list_display = [
        'created_at', 
        'amount',     
        'loan_id',
        'payment_id'
    ]
    list_filter = [
        'amount',
        'loan_id',
        'payment_id'
    ]
    search_fields = ['loan_id', 'amount', 'payment_id']
    class Meta:
        model = PaymentsDetails

admin.site.register(PaymentsDetails, AdminPaymentDetails)