from langchain_community.chat_models.ollama import ChatOllama

def generate_pet_name():
    llm = ChatOllama(model="codellama", temperature=0)
    response = llm.invoke("I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet.")
    return response.content

if __name__ == "__main__":
    print(generate_pet_name())