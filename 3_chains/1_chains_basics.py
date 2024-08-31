from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_community.chat_models.ollama import ChatOllama

model = ChatOllama(model="gemma:2b", temperature=0.1)

messages = [
        ("system", "You are a comedian who tells jokes abour {topic}."),
        ("human", "Tell me {joke_count} jokes.")
        ]
prompt_template = ChatPromptTemplate.from_messages(messages)

# Crating the chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()
response = chain.invoke({"topic": "programmers", "joke_count": 2})
print(response)
