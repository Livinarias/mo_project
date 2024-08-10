from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class Customers(models.Model):
    created_at = models.DateTimeField(blank=True, auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(blank=False, auto_now_add=False, auto_now=True)
    external_id = models.CharField(max_length=60, blank=True, unique=True)
    status = models.SmallIntegerField(blank=True)
    score = models.FloatField(blank=False)
    preapproved_at = models.DateTimeField(blank=False, auto_now_add=False, auto_now=True)
    historical = HistoricalRecords()

    def __str__(self):
        return self.external_id