from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

llm = init_chat_model(model_provider="openai", model="gpt-5-mini")

class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    system_prompt = SystemMessage(content="""You are a helpful female AI assistant that speaks Hindi.""")
    message = llm.invoke([system_prompt] + state["messages"])

    return {"messages": message}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()