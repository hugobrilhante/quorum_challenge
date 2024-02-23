from pathlib import Path
from typing import List

from src.core.data_sourcers import BillCSVDataSource, VoteCSVDataSource, VoteResultCSVDataSource
from src.core.data_sourcers import LegislatorCSVDataSource

DATA_DIR = Path(__file__).resolve().parent / '../../data'


class BaseModel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def all(cls) -> List['BaseModel']:
        return [cls(**item) for item in cls.data_source().get_data()]


class Legislator(BaseModel):
    data_source = LegislatorCSVDataSource


class Bill(BaseModel):
    data_source = BillCSVDataSource


class Vote(BaseModel):
    data_source = VoteCSVDataSource


class VoteResult(BaseModel):
    data_source = VoteResultCSVDataSource
