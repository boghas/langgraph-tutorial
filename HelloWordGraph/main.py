from langgraph.graph import StateGraph # framework that helps designing and managing the flow of tasks in the application using a graph structure
from schemas.agent_schema import AgentState
from nodes.compliment_node import compliment_node

def main():
    name = input("What is your name: ")

    state_graph = StateGraph(AgentState)

    # Add Node to the Graph: Name of the Node | The action it needs to perform
    state_graph.add_node("compliment", compliment_node)

    # Add the START Point: Key : (str) The name of the Starting Node
    state_graph.set_entry_point("compliment")

    # Add the END Point: Key : (str) The name of the Ending Node
    state_graph.set_finish_point("compliment")

    # Compile the Graph
    app = state_graph.compile()

    # Execute the Graph
    result = app.invoke({"message": name})

    # Print the `message` from the AgentState
    print(result["message"])


if __name__ == "__main__":
    main()

