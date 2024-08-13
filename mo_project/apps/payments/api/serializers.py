from rest_framework import serializers

from apps.payments.models import Payments, PaymentsDetails
from apps.utils.search_util import (
    find_customer_variable_by_id,
    find_payment_details_by_payment_id,
    find_customer_by_external_id,
    validate_amout_payment,
    update_status_payment,
    update_loans_records
)


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print("data: ", data)
        data = {
            'external_id': data['external_id'],
            'customer_external_id': find_customer_variable_by_id(
                data,
                'customer_id',
                'external_id'
            ),
            "loans": find_payment_details_by_payment_id(data, 'id')
        }
        return data


class PaymentSerializerPost(serializers.ModelSerializer):

    customer_external_id = serializers.CharField(
        write_only=True, required=True)
    payment_amount = serializers.FloatField(write_only=True, required=True)

    class Meta:
        model = Payments
        fields = ('external_id', 'customer_external_id', 'payment_amount')

    def create(self, validated_data):
        """override create method to organice structure"""
        customer_id = find_customer_by_external_id(
            validated_data, 'customer_external_id')
        validated_data.pop('customer_external_id')
        data_to_detail = {**validated_data}
        validated_data = {
            **validated_data,
            'customer_id': customer_id,
            'total_amount': validated_data['payment_amount']
        }
        validated_data.pop('payment_amount')
        payment_record = Payments.objects.create(**validated_data)
        payment_record.save()
        data_to_detail['payment_id'] = payment_record
        data_to_detail['customer_id'] = customer_id
        self.create_payment_detail(data_to_detail)
        return payment_record

    def create_payment_detail(self, validated_data):
        """Create a payment detail"""
        payment_detail_list, status = validate_amout_payment(validated_data)
        if len(payment_detail_list) > 0:
            PaymentsDetails.\
                objects.bulk_create([PaymentsDetails(**items)
                                    for items in payment_detail_list])
            update_loans_records(payment_detail_list)
        update_status_payment(validated_data['payment_id'], status)
