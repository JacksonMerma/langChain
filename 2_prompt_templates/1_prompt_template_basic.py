from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


# Template with single input
template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)
prompt = prompt_template.invoke({"topic": "cats"})

# Template with multiple inputs
template_multiple = """ You are a helpful assistant.
Human: Tell me a {adjetive} story about a {animal}.
Assistant:"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjetive": "funny", "animal": "dog"})

# Template with system and human messages using tuples
messages = [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes.")
        ]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "programmers", "joke_count": 4})
print(prompt)
