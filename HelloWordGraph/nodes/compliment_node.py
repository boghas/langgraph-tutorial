from schemas.agent_schema import AgentState 


def compliment_node(state: AgentState) -> AgentState:
    """Simple node that adds a compliment message to the state. """

    state["message"] += ", you're doing an amazing job!"

    return state
