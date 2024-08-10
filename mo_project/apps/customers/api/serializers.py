from rest_framework import serializers
from apps.customers.models import Customers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('external_id', 'status', 'score', 'preapproved_at')