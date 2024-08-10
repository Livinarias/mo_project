from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.customers_customer.models import Customers
from apps.customers_customer.api.serializers import CustomerSerializer

@api_view(['GET', 'POST'])
def customers_api_view(request):

    if request.method == 'GET':
        customers = Customers.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return Response(customers_serializer.data)

    if request.method == 'POST':
        data = {**request.data, 'status': 1}
        customers_serializer = CustomerSerializer(data = data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return Response(customers_serializer.data, status=201)
        return Response(customers_serializer.errors, status=400)

@api_view(['GET'])
def customer_detail_view(request, pk):

    if request.method == 'GET':
        customer = Customers.objects.filter(pk=pk).first()
        customer_serializer = CustomerSerializer(customer)
        return Response(customer_serializer.data)
