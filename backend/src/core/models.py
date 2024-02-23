from pathlib import Path
from typing import List

from src.core.parsers import CSVParser

DATA_DIR = Path(__file__).resolve().parent / '../../data'


class Legislator:
    data = CSVParser(DATA_DIR / 'legislators.csv').get_data()

    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name

    @classmethod
    def all(cls) -> List['Legislator']:
        return [cls(**legislator) for legislator in cls.data]


class Bill:
    data = CSVParser(DATA_DIR / 'bills.csv').get_data()

    def __init__(self, id: int, title: str, sponsor_id: int):
        self.id: int = id
        self.title: str = title
        self.sponsor_id: int = sponsor_id

    @classmethod
    def all(cls) -> List['Bill']:
        return [cls(**bill) for bill in cls.data]
