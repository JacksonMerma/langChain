from langchain_community.chat_models.ollama import ChatOllama
from langchain.prompts import PromptTemplate

def generate_pet_name(animal_type, pet_color):
    llm = ChatOllama(model="codellama", temperature=0.7)

    # Defining prompt template
    prompt_template_name = PromptTemplate.from_template(
        "I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
    )
    chain = prompt_template_name | llm
    response = chain.invoke({"animal_type": animal_type, "pet_color": pet_color})
    return response