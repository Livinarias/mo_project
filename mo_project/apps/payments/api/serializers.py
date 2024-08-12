from rest_framework import serializers

from apps.payments.models import Payments, PaymentsDetails
from apps.loans.models import Loans
from apps.utils.search_util import find_customer_variable_by_id, find_loan_by_external_id, find_payment_detail_variable_by_id, find_customer_by_external_id


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print("data: ", data)
        data = {
            'external_id': data['external_id'],
            'customer_external_id': find_customer_variable_by_id(data, 'customer_id', 'external_id'),
            'loan_external_id': find_loan_by_external_id(data, 'external_id'),
            'payment_date': data['paid_at'],
            'total_amount': data['total_amount'],
            'payment_amount': find_payment_detail_variable_by_id(data, 'id', 'amount')
        }
        return data


class PaymentSerializerPost(serializers.ModelSerializer):

    customer_external_id = serializers.CharField(write_only=True, required=True)
    payment_amount = serializers.FloatField(write_only=True, required=True)

    class Meta:
        model = Payments
        fields = ('external_id', 'customer_external_id', 'payment_amount', 'status')
    
    def create(self, validated_data):
        print("create: ", validated_data)
        customer_id = find_customer_by_external_id(validated_data, 'customer_external_id')
        validated_data.pop('customer_external_id')
        data_to_detail = {**validated_data}
        validated_data.pop('payment_amount')
        validated_data = {
            **validated_data,
            'customer_id': customer_id,
            'total_amount': validated_data['payment_amount']
        }
        #get_total_amount(validated_data
        print("total_amount: ", validated_data)
        payment_record = Payments.objects.create(**validated_data)
        payment_record.save()
        data_to_detail['payment_id'] = payment_record
        data_to_detail['customer_id'] = customer_id
        self.create_payment_detail(data_to_detail)
        return payment_record

    def create_payment_detail(self, validated_data):
        payment_detail_data = {
            'amount': validated_data['payment_amount'],
            'payment_id': validated_data['payment_id'],
            'loan_id': Loans.objects.\
                filter(customer_id=validated_data['customer_id']).first()
        }
        payment_detail_record = PaymentsDetails.\
            objects.create(**payment_detail_data)
        payment_detail_record.save()