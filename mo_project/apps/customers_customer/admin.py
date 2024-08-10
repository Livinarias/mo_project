from django.contrib import admin
from apps.customers_customer.models import Customers


class AdminCustomer(admin.ModelAdmin):
    list_display = ['created_at', 'external_id', 'status', 'score', 'updated_at', 'preapproved_at']
    list_filter = ['external_id', 'status', 'score']
    list_editable = ['score', 'status']
    search_fields = ['external_id', 'score']
    class Meta:
        model = Customers

admin.site.register(Customers, AdminCustomer)