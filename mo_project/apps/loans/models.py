from django.db import models
from apps.customers.models import Customers
from simple_history.models import HistoricalRecords


# Create your models here.
class Loans(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    external_id = models.CharField(max_length=60, unique=True, blank=False)
    amount = models.FloatField(blank=False)
    status = models.SmallIntegerField(blank=False)
    contract_version = models.CharField(max_length=60, unique=True, blank=False)
    maximum_payment_date = models.DateTimeField(blank=True, auto_now=True)
    taken_at = models.DateTimeField(blank=True, auto_now=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name='Customer')
    historical = HistoricalRecords()
    outstanding = models.FloatField(blank=False)