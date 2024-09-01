from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_community.chat_models.ollama import ChatOllama
from langchain.schema.runnable import RunnableLambda

model = ChatOllama(model="gemma:2b", temperature=0.1)

messages = [
        ("system", "You are a comedian who tells jokes abour {topic}."),
        ("human", "Tell me {joke_count} jokes.")
        ]
prompt_template = ChatPromptTemplate.from_messages(messages)

# Defining additional processing steps using RunnableLambda
uppercase_output = RunnableLambda(lambda x: x.upper())
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")

# Creating the chain
chain = prompt_template | model | StrOutputParser() | uppercase_output | count_words
response = chain.invoke({"topic": "programmers", "joke_count": 2})
print(response)
