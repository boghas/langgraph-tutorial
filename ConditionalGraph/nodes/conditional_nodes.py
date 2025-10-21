from states.agent_state import AgentState


def conditional_node1(state: AgentState) -> AgentState:
    """Conditional node1; Decide what node to execute next based on `operation1`."""

    if state["operation1"] == "+":
        return "addition1"
    elif state["operation1"] == "-":
        return "substraction1"

def conditional_node2(state: AgentState) -> AgentState:
    """Conditional node2; Decide what node to execute next based on `operation2`."""

    if state["operation2"] == "+":
        return "addition2"
    elif state["operation2"] == "-":
        return "substraction2"  