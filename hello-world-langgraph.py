"""
Hello World example using LangGraph.
"""

from typing import TypedDict
from langgraph.graph import StateGraph


# Define the state that flows through the graph
class AgentState(TypedDict):
    message: str


# A simple node that changes the message
def greeting_node(state: AgentState) -> AgentState:
    state["message"] = f"Hey {state['message']}, how is your day going?"
    return state


# Build the graph
graph = StateGraph(AgentState)
graph.add_node("greeter", greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

# Compile into an app
app = graph.compile()

# Draw the graph as an image
png_bytes = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png_bytes)

# Run the app with an input
result = app.invoke({"message": "Bob"})
print("Result:", result["message"])

# Result: Hey Bob, how is your day going?