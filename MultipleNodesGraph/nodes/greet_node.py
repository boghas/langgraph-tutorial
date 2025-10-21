from states.agent_state import AgentState


def greet_user(state: AgentState) -> AgentState:
    """Greet the user."""

    state["result"] = f"{state["name"]}, welcome to the system!"

    return state