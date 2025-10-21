from langgraph.graph import StateGraph
from states.agent_state import State
from nodes.operation_node import perform_operation_on_node


def main():
    entry = {"name": "Jack Sparrow", "values": [1, 2, 3, 4], "operation": "+"}

    graph = StateGraph(State)

    graph.add_node("operations_node", perform_operation_on_node)

    graph.set_entry_point("operations_node")
    graph.set_finish_point("operations_node")

    app = graph.compile()

    result = app.invoke(entry)

    print(result["result"])

if __name__ == "__main__":
    main()
