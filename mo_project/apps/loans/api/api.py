from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from apps.loans.models import Loans
from apps.loans.api.serializers import LoansSerializer, LoansSerializerPost
from apps.utils.search_util import find_customer_by_external_id

@api_view(['GET', 'POST'])
def create_loans_api_view(request):

    if request.method == 'GET':
        loans = Loans.objects.all()
        print("loans:", loans)
        loans_serializer = LoansSerializer(loans, many=True)
        print("loans_serializer:", loans_serializer)
        return Response(loans_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = {**request.data, 'status': 1}
        print("request data:", data)
        loans_serializer = LoansSerializerPost(data = data)
        if loans_serializer.is_valid():
            print("serializer valid")
            loans_serializer.save()
            return Response(loans_serializer.data, status=status.HTTP_201_CREATED)
        return Response(loans_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_loan_by_customer_view(request, pk):

    if request.method == 'GET':
        customer_id = find_customer_by_external_id({'customer_external_id': pk}, 'customer_external_id')
        loan = Loans.objects.filter(customer_id=customer_id)
        loan_serializer = LoansSerializer(loan, many=True)
        return Response(loan_serializer.data, status=status.HTTP_200_OK)
