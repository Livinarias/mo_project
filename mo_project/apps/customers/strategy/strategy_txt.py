from typing import ByteString
from apps.customers.strategy.interface.strategy_interface import StrategyInterface

class ConcreteStrategyTXT(StrategyInterface):


    def recieve_data(self, data: ByteString) -> ByteString:
        """Reorganize data to create records"""
        return data.read().decode('utf-8').splitlines()