from django.contrib import admin

from apps.customers.models import Customers


class AdminCustomer(admin.ModelAdmin):
    """class to admin customers model in django"""

    list_display = ['created_at', 'external_id',
                    'status', 'score', 'updated_at', 'preapproved_at']
    list_filter = ['external_id', 'status', 'score']
    search_fields = ['external_id', 'score']

    class Meta:
        model = Customers


admin.site.register(Customers, AdminCustomer)
