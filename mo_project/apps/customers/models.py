from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class Customers(models.Model):
    """class to model customers"""

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    external_id = models.CharField(max_length=60, unique=True, blank=False)
    status = models.SmallIntegerField(blank=False)
    score = models.FloatField(blank=False)
    preapproved_at = models.DateTimeField(blank=True, auto_now=True)
    historical = HistoricalRecords()

    def __str__(self):
        return self.external_id