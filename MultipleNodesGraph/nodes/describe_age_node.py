from states.agent_state import AgentState


def describe_user_age(state: AgentState) -> AgentState:
    """Describe the user's age."""

    state["result"] += f" You are {state["age"]} years old!"

    return state