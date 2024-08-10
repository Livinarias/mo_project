import csv
from apps.customers.strategy.interface.strategy_interface import StrategyInterface
from typing import ByteString


class ConcreteStrategyCSV(StrategyInterface):


    def recieve_data(self, data: ByteString) -> ByteString:
        """Reorganize data to create records"""
        file = data.read().decode('utf-8')
        return csv.reader(file.splitlines())
