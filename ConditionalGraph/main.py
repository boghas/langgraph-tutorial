from langgraph.graph import StateGraph, START, END
from nodes import addition_node, substraction_node, conditional_nodes
from states.agent_state import AgentState


def main():
    data = {"number1": 5, "number2": 10, "operation1": "+", "number3": 5, "number4": 10, "operation2": "-"}

    graph = StateGraph(AgentState)

    graph.add_node("addition1", addition_node.addition_node1)
    graph.add_node("addition2", addition_node.addition_node2)
    graph.add_node("substraction1", substraction_node.substraction_node1)
    graph.add_node("substraction2", substraction_node.substraction_node2)
    graph.add_node("router1", lambda state: state)
    graph.add_node("router2", lambda state: state)

    graph.add_edge(START, "router1")

    list_map1 = {
        "addition1": "addition1",
        "substraction1": "substraction1"
    }

    graph.add_conditional_edges(
        "router1",
        conditional_nodes.conditional_node1,
        list_map1
    )

    graph.add_edge("addition1", "router2")
    graph.add_edge("substraction1", "router2")

    list_map2 = {
        "addition2": "addition2",
        "substraction2": "substraction2"
    }

    graph.add_conditional_edges(
        "router2",
        conditional_nodes.conditional_node2,
        list_map2
    )

    graph.add_edge("addition2", END)
    graph.add_edge("substraction2", END)

    app = graph.compile()

    result = app.invoke(data)

    print(result)

if __name__ == "__main__":
    main()
