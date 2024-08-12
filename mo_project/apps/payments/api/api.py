from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from apps.payments.models import Payments
from apps.payments.api.serializers import PaymentSerializer, PaymentSerializerPost
from apps.utils.search_util import find_customer_by_external_id


@api_view(['GET','POST'])
def create_payments_api_view(request):

    if request.method == 'GET':
        payments = Payments.objects.all()
        payments_serializer = PaymentSerializer(payments, many=True)
        return Response(payments_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        payments_serializer = PaymentSerializerPost(data=request.data)
        if payments_serializer.is_valid():
            payments_serializer.save()
            return Response(payments_serializer.data, status=status.HTTP_201_CREATED)
        return Response(payments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_payment_by_customer_view(request, pk):

    if request.method == 'GET':
        customer_id = find_customer_by_external_id({'external_id': pk}, 'external_id')
        payment = Payments.objects.filter(customer_id=customer_id)
        payment_serializer = PaymentSerializer(payment, many=True)
        return Response(payment_serializer.data, status=status.HTTP_200_OK)