from langchain.messages import SystemMessage, ToolMessage
from calculator.state import MessagesState
from calculator.tools import model_with_tools, tools_by_name
from langgraph.graph import START, END, StateGraph

def llm_call(state: dict):
    """Call the LLM with the tools."""
    
    return {
        "messages": [
            model_with_tools.invoke(
                [
                SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs.")
                ] + state["messages"]
            )
        ],
        "llm_calls": state.get("llm_calls", 0) + 1
    }
    
    
# ===== Tool node =====
def tool_node(state: dict):
    """Peforms the tool call"""
    result = []
    
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
        
    return {"messages": result}


# ===== End node =====
def should_continue(state: MessagesState):
    """Decide if the conversation should continue."""
    messages = state["messages"]
    last_message = messages[-1]
    
    if last_message.tool_calls:
        return "tool_node"
    
    return END