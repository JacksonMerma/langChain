from langchain_community.chat_models.ollama import ChatOllama

# Creating gemma model
model = ChatOllama(model="gemma:2b", temperature=0)

# Invoke the model with the message
response = model.invoke("What is competitive programming?")
print(f"Full result: {response}")
print(f"Content only: {response.content}")
