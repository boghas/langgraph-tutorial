from states.agent_state import State


def perform_operation_on_node(state: State) -> State:
    """Multiplies or Adds the state values based on state's operation parameter."""

    if state["operation"] == "*":
        multiplication = 1
        for value in state["values"]:
            multiplication *= value
        state["result"] = (
            f"Hi {state["name"]}, your answer is: {multiplication}"
        )
    
    elif state["operation"] == "+":
        state["result"] = (
            f"Hi {state["name"]}, your answer is: {sum(state["values"])}"
        )

    else:
        raise ValueError(f"Unsported operation: {state["operation"]}! Available operations are: `*` or `+`.")
       
    return state