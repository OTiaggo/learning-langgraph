from dotenv import load_dotenv
from langchain.tools import tool
from langchain.chat_models.base import init_chat_model

load_dotenv()

model = init_chat_model(
    "deepseek-v4-pro",
    temperature=0,
    model_kwargs={"extra_body": {"thinking": {"type": "disabled"}}},
)


# ===== Tools =====
@tool  
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@tool 
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@tool
def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b

@tool
def divide(a: int, b: int) -> int:
    """Divide a by b."""
    return a / b

# LLM with tools
tools = [multiply, add, subtract, divide]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)

