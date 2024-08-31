from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


# Template with single input
template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)
prompt = prompt_template.invoke({"topic": "cats"})
print(prompt)
