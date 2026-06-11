from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from tools import *

query = "Whats the sum of all districts in kerala and tamilnadu? and whats the capital of kerala?"
llm = init_chat_model("llama3.2", model_provider="ollama")
agent = create_agent(llm, tools=tools)

response = agent.invoke(
    {"messages": 
     [ {
          "role" : "user",
          "content" : query 
        }
         
     ]
 })

print(response["messages"][-1].content)