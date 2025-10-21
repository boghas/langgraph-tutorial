from typing import TypedDict, List


class State(TypedDict):
    name: str
    values: list[int]
    operation: str
    result: str

