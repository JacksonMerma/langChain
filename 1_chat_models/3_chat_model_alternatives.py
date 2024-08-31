from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.chat_models.ollama import ChatOllama

messages = [
        SystemMessage(content="Solve the next math problem"),
        HumanMessage(content="What is 2 times 5?")
        ]

# Defining models
gemma_model = ChatOllama(model="gemma:2b", temperature=0)
codellama_model = ChatOllama(model="codellama", temperature=0)

gemma_response = gemma_model.invoke(messages)
codellama_response = codellama_model.invoke(messages)

print(f"Gemma: {gemma_response.content}")
print(f"Codellama: {codellama_response.content}")
