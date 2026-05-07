from langgraph.graph import START, END
from nodes import llm_call, tool_node, should_continue
from state import MessagesState
from langgraph.graph import StateGraph


# Build workflow
agent_builder = StateGraph(MessagesState)
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)


# Add edges to connect nodes
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges("llm_call", should_continue, ["tool_node", END])
agent_builder.add_edge("tool_node", "llm_call")


# Compile
agent = agent_builder.compile()


# Show
from IPython.display import Image, display

png_bytes = agent.get_graph(xray=True).draw_mermaid_png()

with open("calculator/graph.png", "wb") as f:
    f.write(png_bytes)


# Invoke
