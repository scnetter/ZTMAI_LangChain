import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
import openai

load_dotenv(find_dotenv(), override=True)

llm = ChatOpenAI()
//output = llm.invoke('Explain quantum mechanics in one sentence')

from langchain.schema import(
    SystemMessage, # System
    AIMessage, # Assistant
    HumanMessage, # user
)

messages = [
    SystemMessage(content='You are a physicist and respond only in German.'),
    HumanMessage(content='Can you explain quantum mechanics in one sentence?'),
    # AImessage will be returned from llm.invoke()
]

output = llm.invoke(messages)
print(output.content)