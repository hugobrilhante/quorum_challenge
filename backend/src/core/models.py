from dataclasses import dataclass


@dataclass(frozen=True)
class Legislator:
    id: int
    name: str


@dataclass(frozen=True)
class Bill:
    id: int
    title: str
    sponsor_id: int
