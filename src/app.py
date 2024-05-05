from langchain import LLM, OpenAI
from langchain.llms import OpenAI
import config
llm = OpenAI(openai_api_key=config.OPENAI_API_KEY,temperature=config.TEMPERATURE, system_message=config.SYSTEM_MESSAGE)

def ask_llm(query):
    if not query:
        raise ValueError("Query cannot be empty")
    return llm.predict(prompt=query)

res = ask_llm("What is the meaning of life?")

print(res)