from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek

# llm = ChatOpenAI(model="gpt-5-nano")
llm = ChatDeepSeek(model="deepseek-v4-pro", model_kwargs={"extra_body": {"thinking": {"type": "disabled"}}})