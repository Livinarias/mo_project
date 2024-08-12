from apps.customers.models import Customers
from apps.loans.models import Loans
from apps.payments.models import PaymentsDetails, Payments


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


def find_customer_by_external_id(data, variable_search) -> Customers | None:
    """method to return instance to customer filter by external id"""
    try:
        return Customers.objects.get(
            external_id=data[f'{variable_search}'])
    except Customers.DoesNotExist:
        print("Customer not found")
        return None


"""Utilitys to module Loans"""


def find_payment_details_by_payment_id(data, variable_search) -> list[dict]:
    """method to return instance to loan filter by external id"""
    try:
        payment_details_obj = PaymentsDetails.objects.filter(
            payment_id=data[f"{variable_search}"],
            )
        payment_detail_list = []
        for record in payment_details_obj:
            payment_detail_list.append({
                "loan_external_id": record.loan_id.external_id,
                "payment_date": record.loan_id.created_at,
                "status": record.payment_id.status,
                'total_amount': record.payment_id.total_amount,
                "payment_amount": record.amount
            })
        return payment_detail_list
    except PaymentsDetails.DoesNotExist:
        #FIXME probar que no se totee
        print("Loan not found")
        return [{}]


def find_loan_variable_by_id(data, variable_search, variable_need) -> str:
    """method to return variable to loan filter by id"""
    try:
        return Loans.objects.filter(
            id=data[f'{variable_search}']).\
            values(f'{variable_need}')[0].get(f'{variable_need}')
    except IndexError:
        print("Loan not found")
        return None


def validation_status(status: int, loan: Loans) -> bool:
    """method to validate status of loan"""
    if status == 3 and loan.status >= 2:
        return False
    if status == 4:
        return False
    return True


"""Utilitys to module Payments"""


def find_payment_detail_variable_by_payment_id(data, variable_search, variable_need) -> str:
    """method to return variable to payment detail filter by id"""
    try:
        return PaymentsDetails.objects.filter(
            payment_id=data[f'{variable_search}']).\
            values(f'{variable_need}')[0].get(f'{variable_need}')
    except IndexError:
        print("payment detail not found")
        return None


def active_credits(status: int) -> str:
    if status != 2:
        return False
    return True


def validate_amout_payment(validated_data: list[dict]) -> list[dict]:
    loans_list = []
    try:
        loans = Loans.objects.\
            filter(
                customer_id=validated_data['customer_id'],
                status=2).order_by('id')
        total_loan = sum([item.outstanding for item in loans])
        if validated_data['payment_amount'] <= total_loan:
            paid = validated_data['payment_amount']
            for item in loans:
                if total_loan >= 0:
                    loans_list.append(
                        {
                            'amount': item.outstanding if paid > item.outstanding else paid,
                            'payment_id': validated_data['payment_id'],
                            'loan_id': item,
                        }
                    )
                paid -= item.outstanding
            return loans_list, 1
        return loans_list, 2

    except Exception as e:
        print("Error: ", e)
        return loans_list, 2


def update_status_payment(instance: Payments, status: int) -> None:
    instance.status = status
    instance.save()


def update_loans_records(payment_detail_list: list[dict]) -> None:
    for item in payment_detail_list:
        item['loan_id'].outstanding -= item['amount']
        item['loan_id'].status = 4 if item['loan_id'].\
            outstanding == 0 else item['loan_id'].status
        item['loan_id'].save()
