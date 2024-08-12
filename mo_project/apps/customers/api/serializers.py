from rest_framework import serializers

from apps.customers.models import Customers
from apps.utils.search_util import find_total_debt


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('external_id', 'status', 'score', 'preapproved_at')


class CustomerBalanceSerializer(serializers.ModelSerializer):

    available_amount = serializers.FloatField(write_only=True, required=True)
    total_debt = serializers.FloatField(write_only=True, required=True)
    class Meta:
        model = Customers
        fields = ('id', 'external_id', 'score', 'available_amount', 'total_debt')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        total_debt = find_total_debt(data)
        data = {
            'external_id': data['external_id'],
            'score': data['score'],
            'available_amount': data['score'] - total_debt,
            'total_debt': total_debt
        }
        return data
