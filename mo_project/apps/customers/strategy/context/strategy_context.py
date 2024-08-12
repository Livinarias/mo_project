from typing import ByteString
from apps.customers.strategy.interface.strategy_interface import StrategyInterface
from apps.customers.models import Customers
from apps.customers.enums.custumers_enums import ExtensionFiles


# Concrete Strategies implement the Strategy interface.
class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: StrategyInterface) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> StrategyInterface:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: StrategyInterface) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def create_customer(self, data: ByteString, extension_file: str) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        result = self._strategy.recieve_data(data)
        if extension_file == ExtensionFiles.CSV.value:
            for row in result:
                external_id, status, score = row
                try:
                    Customers.objects.create(
                        external_id=external_id,
                        status=status,
                        score=score
                    )
                except Exception as e:
                    print(f"Error creating customer: {e}")