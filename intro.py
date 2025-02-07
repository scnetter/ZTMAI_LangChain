import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
import openai

load_dotenv(find_dotenv(), override=True)

llm = ChatOpenAI()
output = llm.invoke('Explain quantum mechanics in one sentence')
print(output.content)
