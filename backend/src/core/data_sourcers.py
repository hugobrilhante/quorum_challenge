from abc import ABC
from abc import abstractmethod
from pathlib import Path

from src.core.parsers import CSVParser

DATA_DIR = Path(__file__).resolve().parent / '../../data'


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class LegislatorCSVDataSource(DataSource):
    def get_data(self):
        return CSVParser(DATA_DIR / 'legislators.csv').load_data()


class BillCSVDataSource(DataSource):
    def get_data(self):
        return CSVParser(DATA_DIR / 'bills.csv').load_data()
