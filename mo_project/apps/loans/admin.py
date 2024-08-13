from django.contrib import admin

from apps.loans.models import Loans


class AdminLoans(admin.ModelAdmin):
    """class to admin loans model in django"""

    list_display = [
        'created_at', 
        'external_id',
        'amount',
        'status',
        'contract_version', 
        'maximum_payment_date', 
        'taken_at',
        'customer_id', 
        'outstanding'
    ]
    list_filter = [
        'external_id',
        'status',
        'amount',
        'contract_version',
        'customer_id',
        'outstanding'
    ]
    search_fields = ['external_id', 'status', 'amount', 'customer_id']
    class Meta:
        model = Loans

admin.site.register(Loans, AdminLoans)