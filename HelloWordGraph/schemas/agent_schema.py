from typing import Dict, TypedDict


class AgentState(TypedDict):
    """State schema.
    A shared data structure that keeps track of information as the application runs.
    """
    
    message : str