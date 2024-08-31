from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models.ollama import ChatOllama
from langchain.schema.runnable import RunnableLambda, RunnableSequence

model = ChatOllama(model="gemma:2b", temperature=0.1)

messages = [
        ("system", "You are a comedian who tells jokes abour {topic}."),
        ("human", "Tell me {joke_count} jokes.")
        ]
prompt_template = ChatPromptTemplate.from_messages(messages)

# Create individual runnables
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parser_output = RunnableLambda(lambda x: x.content)

# Creating the sequence
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parser_output)
response = chain.invoke({"topic": "programmers", "joke_count": 2})
print(response)
