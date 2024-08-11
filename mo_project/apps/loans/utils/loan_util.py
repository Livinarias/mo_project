from apps.customers.models import Customers


def find_customer_variable_by_id(data, variable_search, variable_need) -> str:
    return Customers.objects.filter(
            id=data[f'{variable_search}']).\
                values(f'{variable_need}')[0].get(f'{variable_need}')

def find_customer_variable_by_external_id(data, variable_search) -> Customers:
    return Customers.objects.get(
            external_id=data[f'{variable_search}'])