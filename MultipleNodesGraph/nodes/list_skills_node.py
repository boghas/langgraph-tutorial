from states.agent_state import AgentState


def list_user_skills(state: AgentState) -> AgentState:
    """List the user's skills."""

    state["result"] += f" You have skills in: {", ".join(state["skills"])}"

    return state