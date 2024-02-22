from dataclasses import dataclass


@dataclass(frozen=True)
class Legislator:
    id: int
    name: str
