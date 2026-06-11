from langchain.agents import create_agent
from langchain_core.messages import HumanMessage ,AIMessage

from langchain.chat_models import init_chat_model

from tools import *


def convo_agent():
    llm = init_chat_model("llama3.2",model_provider="ollama")
    tools = [area]
    query1="whats the area of a rectangle with length 4 and width 3?"
    agent = create_agent(llm, tools=tools)
    messages = agent.invoke({"messages":[{"role":"user","content":query1}]})
    message_history = messages["messages"]
    query2="what about one with sides 4,2?"
    messages=agent.invoke({"messages":message_history +[{"role":"user","content":query2}]})
    
    # filter out the AI messages

    filtered_messages = [msg for msg in messages["messages"] if isinstance(msg,(HumanMessage, AIMessage)) and msg.content.strip()]
    for msg in filtered_messages:
        print(f"{msg.__class__.__name__}: {msg.content}")
def main():
    convo_agent()

if __name__ == "__main__":
    main()