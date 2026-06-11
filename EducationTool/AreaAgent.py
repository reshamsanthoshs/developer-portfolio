import sys

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from tools import *

def call_agent(query):
    tools = [area]
    print(f"Query: {query}")
    llm = init_chat_model("llama3.2", model_provider="ollama")
    agent = create_agent(llm, tools=tools)
    response = agent.invoke({"messages":[{"role":"user","content":"query"}]})
    print(response["messages"][-1].content)

def main():
    query = " ".join(sys.argv[1:])

    if not query:
        print("Usage: python AreaAgent.py <query>")
        return

    call_agent(query)

if __name__ == "__main__":
    main()