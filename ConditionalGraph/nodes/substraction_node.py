from states.agent_state import AgentState

def substraction_node1(state: AgentState) -> AgentState:
    """Substracts two numbers togheter."""

    state["final_number1"] = state["number1"] - state["number2"]

    return state

def substraction_node2(state: AgentState) -> AgentState:
    """Substracts two numbers togheter."""

    state["final_number2"] = state["number3"] - state["number4"]

    return state