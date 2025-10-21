from states.agent_state import AgentState


def addition_node1(state: AgentState) -> AgentState:
    """Adds two numbers togheter."""

    state["final_number1"] = state["number1"] + state["number2"]

    return state

def addition_node2(state: AgentState) -> AgentState:
    """Adds two numbers togheter."""

    state["final_number2"] = state["number3"] + state["number4"]

    return state