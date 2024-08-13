from django.db import models
from simple_history.models import HistoricalRecords
from apps.customers.models import Customers
from apps.loans.models import Loans


class Payments(models.Model):
    """Class to model Payments"""

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    external_id = models.CharField(max_length=60, unique=True, blank=False, null=False)
    total_amount = models.FloatField(blank=False, null=False)
    status = models.SmallIntegerField(blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, auto_now=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name='Customer', null=False)
    historical = HistoricalRecords()

    def __str__(self):
        return self.external_id


class PaymentsDetails(models.Model):
    """class to model Payments Details"""

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    amount = models.FloatField(blank=False, null=False)
    loan_id = models.ForeignKey(Loans, on_delete=models.CASCADE, verbose_name='Loans', null=False)
    payment_id = models.ForeignKey(Payments, on_delete=models.CASCADE, verbose_name='Payments', null=False)
    historical = HistoricalRecords()