from typing import TypedDict, List


class AgentState(TypedDict):
    name: str
    age: int
    skills: List[str]
    result: str