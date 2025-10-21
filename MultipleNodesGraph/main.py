from langgraph.graph import StateGraph
from nodes import describe_age_node, greet_node, list_skills_node
from states.agent_state import AgentState

def main():
    args = {"name": "Linda", "age": 31, "skills": ["Python", "LangGraph", "LangChain"]}

    graph = StateGraph(AgentState)

    graph.add_node("greet", greet_node.greet_user)
    graph.add_node("describe_age", describe_age_node.describe_user_age)
    graph.add_node("list_skills", list_skills_node.list_user_skills)

    graph.set_entry_point("greet")
    graph.add_edge("greet", "describe_age")
    graph.add_edge("describe_age", "list_skills")

    graph.set_finish_point("list_skills")

    app = graph.compile()

    result = app.invoke(args)

    print(result["result"])

if __name__ == "__main__":
    main()
