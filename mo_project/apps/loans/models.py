from django.db import models
from simple_history.models import HistoricalRecords
from apps.customers.models import Customers


# Create your models here.
class Loans(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    external_id = models.CharField(max_length=60, unique=True, blank=False, null=False)
    amount = models.FloatField(blank=False, null=False)
    status = models.SmallIntegerField(blank=False, null=False)
    contract_version = models.CharField(max_length=60, blank=True, null=True)
    maximum_payment_date = models.DateTimeField(blank=True, auto_now=True)
    taken_at = models.DateTimeField(blank=True, auto_now=True)
    outstanding = models.FloatField(blank=False)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name='Customer', null=False)
    historical = HistoricalRecords()

    def __str__(self) -> str:
        return self.external_id