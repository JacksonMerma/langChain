from langchain_community.chat_models.ollama import ChatOllama
from langchain.prompts import PromptTemplate

def generate_pet_name(animal_type):
    llm = ChatOllama(model="codellama", temperature=0)

    # Defining prompt template
    prompt_template_name = PromptTemplate.from_template(
        "I have a {animal_type} pet and I want a cool name for it. Suggest me five cool names for my pet."
    )
    chain = prompt_template_name | llm
    response = chain.invoke({"animal_type": animal_type})
    return response

if __name__ == "__main__":
    print(generate_pet_name("cat"))