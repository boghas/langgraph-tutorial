from typing import TypedDict, Union

class AgentState(TypedDict):
    number1: Union[int, float]
    number2: Union[int, float]
    operation1: str
    number3: Union[int, float]
    number4: Union[int, float]
    operation2: str
    final_number1: float
    final_number2: float
