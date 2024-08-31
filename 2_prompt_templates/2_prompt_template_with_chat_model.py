from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models.ollama import ChatOllama

model = ChatOllama(model="gemma:2b", temperature=0.4)

# Template with single input
template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)
prompt = prompt_template.invoke({"topic": "cats"})
response = model.invoke(prompt)
print(response.content)

# Template with multiple inputs
template_multiple = """ You are a helpful assistant.
Human: Tell me a {adjetive} story about a {animal}.
Assistant:"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjetive": "funny", "animal": "dog"})
reponse = model.invoke(prompt)
print(reponse.content)

# Template with system and human messages using tuples
messages = [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes.")
        ]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "programmers", "joke_count": 4})
reponse = model.invoke(prompt)
print(reponse.content)
