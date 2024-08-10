from abc import ABC, abstractmethod
from typing import ByteString


class StrategyInterface(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def recieve_data(self, data: ByteString) -> ByteString:
        pass
