from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from apps.customers.models import Customers
from apps.customers.api.serializers import CustomerSerializer, CustomerBalanceSerializer

@api_view(['GET', 'POST'])
def customers_api_view(request):

    if request.method == 'GET':
        customers = Customers.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return Response(customers_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = {**request.data, 'status': 2}
        customers_serializer = CustomerSerializer(data = data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return Response(customers_serializer.data, status=status.HTTP_201_CREATED)
        return Response(customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def customer_detail_view(request, pk):

    if request.method == 'GET':
        customer = Customers.objects.filter(external_id=pk).first()
        customer_serializer = CustomerSerializer(customer)
        return Response(customer_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_balance_view(request, pk):

    if request.method == 'GET':
        customer = Customers.objects.filter(external_id=pk).first()
        customer_serializer = CustomerBalanceSerializer(customer)
        return Response(customer_serializer.data, status=status.HTTP_200_OK)
