from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_community.chat_models.ollama import ChatOllama

model = ChatOllama(model="gemma:2b", temperature=0)

# Defining messages
## System message = context
## Human message = message from user to the model
## AI message = response

#messages = [
#        SystemMessage(content="answer as an expert in contests"),
#        HumanMessage(content="what is competitive programming?")
#        ]

# Invoke the model with the messages
#response = model.invoke(messages)
#print(response.content)

# Using IA message
messages = [
        SystemMessage(content="Solve the next problem as an experto in math"),
        HumanMessage(content="What is 100/5?"),
        AIMessage(content="It's 20"),
        HumanMessage(content="And divided by 10?")
        ]

response = model.invoke(messages)
print(response.content)
