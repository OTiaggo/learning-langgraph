from calculator.build_compile import agent
from langchain.messages import HumanMessage

messages = [
    HumanMessage(content="Add 3 and 4."),
    HumanMessage(content="Multiply the result by 2."),
    HumanMessage(content="Subtract 1 from the result."),
    HumanMessage(content="Divide the result by 2."),
]
messages = agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()