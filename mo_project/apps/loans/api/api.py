from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from apps.loans.models import Loans
from apps.loans.api.serializers import LoansSerializer, LoansSerializerPost

@api_view(['GET', 'POST'])
def create_loans_api_view(request):

    if request.method == 'GET':
        customers = Loans.objects.all()
        customers_serializer = LoansSerializer(customers, many=True)
        return Response(customers_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = {**request.data, 'status': 2}
        print("request data:", data)
        customers_serializer = LoansSerializerPost(data = data)
        if customers_serializer.is_valid():
            print("serializer valid")
            customers_serializer.save()
            return Response(customers_serializer.data, status=status.HTTP_201_CREATED)
        return Response(customers_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_loan_by_customer_view(request, pk):

    if request.method == 'GET':
        print("request method:", request)
        customer = Loans.objects.get(customer_id=pk)
        customer_serializer = LoansSerializer(customer)
        return Response(customer_serializer.data, status=status.HTTP_200_OK)
