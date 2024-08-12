from apps.customers.models import Customers
from apps.loans.models import Loans
from apps.payments.models import PaymentsDetails


"""Utilitys to module Customers"""
def find_customer_variable_by_id(data, variable_search, variable_need) -> str:
    """method to return variable to customer filter by id"""
    try:
        return Customers.objects.filter(
                id=data[f'{variable_search}']).\
                    values(f'{variable_need}')[0].get(f'{variable_need}')
    except IndexError:
        print("Customer not found")
        return None

def find_customer_by_external_id(data, variable_search) -> Customers:
    """method to return instance to customer filter by external id"""
    try:
        return Customers.objects.get(
                external_id=data[f'{variable_search}'])
    except Customers.DoesNotExist:
        print("Customer not found")
        return None


"""Utilitys to module Loans"""
def find_loan_by_external_id(data, variable_search) -> Loans:
    """method to return instance to loan filter by external id"""
    try:
        return Loans.objects.get(
                external_id=data[f'{variable_search}'])
    except Loans.DoesNotExist:
        print("Loan not found")
        return None

def find_loan_variable_by_id(data, variable_search, variable_need) -> str:
    """method to return variable to loan filter by id"""
    try:
        return Loans.objects.filter(
                id=data[f'{variable_search}']).\
                    values(f'{variable_need}')[0].get(f'{variable_need}')
    except IndexError:
        print("Loan not found")
        return None

def validation_status(status: str, loan: Loans) -> bool:
    """method to validate status of loan"""
    print("loan validation", loan.status)
    if status == 3 and loan.status not in (3, 2, 4):
        return False
    if status == 4:
        return False
    return True


"""Utilitys to module Payments Details"""
def find_payment_detail_variable_by_id(data, variable_search, variable_need) -> str:
    """method to return variable to payment detail filter by id"""
    try:
        return PaymentsDetails.objects.filter(
                id=data[f'{variable_search}']).\
                    values(f'{variable_need}')[0].get(f'{variable_need}')
    except IndexError:
        print("payment detail not found")
        return None