from typing import List

from .data_sourcers import BillCSVDataSource
from .data_sourcers import LegislatorCSVDataSource
from .data_sourcers import VoteCSVDataSource
from .data_sourcers import VoteResultCSVDataSource


class BaseModel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def all(cls) -> List['BaseModel']:
        return [cls(**item) for item in cls.data_source().get_data()]

    @classmethod
    def get(cls, **kwargs) -> 'BaseModel':
        items = cls.all()
        filtered_data = [item for item in items if cls._matches_filters(item, kwargs)]
        if len(filtered_data) == 0:
            raise ValueError(f'{cls.__name__} not found')
        elif len(filtered_data) > 1:
            raise ValueError('Multiple items found')
        return filtered_data[0]

    @classmethod
    def filter(cls, **kwargs) -> List['BaseModel']:
        items = cls.all()
        filtered_data = [item for item in items if cls._matches_filters(item, kwargs)]
        return filtered_data

    @classmethod
    def _matches_filters(cls, item, filters) -> bool:
        for key, value in filters.items():
            if getattr(item, key, None) != str(value):
                return False
        return True


class Legislator(BaseModel):
    data_source = LegislatorCSVDataSource


class Bill(BaseModel):
    data_source = BillCSVDataSource


class Vote(BaseModel):
    data_source = VoteCSVDataSource


class VoteResult(BaseModel):
    data_source = VoteResultCSVDataSource
