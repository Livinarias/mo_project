from rest_framework import serializers

from apps.loans.models import Loans
from apps.utils.search_util import find_customer_variable_by_id, find_customer_by_external_id


class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print("data: {}".format(data))
        customer_external_id = find_customer_variable_by_id(data, 'customer_id', 'external_id')
        data = {
            'external_id': data['external_id'],
            'customer_external_id': customer_external_id,
            'amount': data['amount'],
            'outstanding': data['outstanding'],
            'status': data['status']
        }
        return data


class LoansSerializerPost(serializers.ModelSerializer):

    customer_external_id = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Loans
        fields = ('external_id',
                'customer_external_id',
                'amount',
                'outstanding',
                'status'
            )
        
    def create(self, validated_data):
        print("create: ", validated_data)
        customer_id = find_customer_by_external_id(validated_data, 'customer_external_id')
        validated_data.pop('customer_external_id')
        validated_data = {**validated_data, 'customer_id': customer_id}
        loan_record = Loans.objects.create(**validated_data)
        loan_record.save()
        return loan_record