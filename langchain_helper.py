from langchain_community.chat_models.ollama import ChatOllama
from langchain.prompts import PromptTemplate
#from langchain.output_parsers import XMLOutputParser
#from typing_extensions import TypedDict, Annotated
from langchain.agents import load_tools, initialize_agent, AgentType

"""
class Answer(TypedDict):
    names: Annotated[str, ..., "Pet names"]
"""

def generate_pet_name(animal_type, pet_color):
    llm = ChatOllama(model="codellama", temperature=0.7)
    #structured_llm = llm.with_structured_output(Answer)

    # Defining prompt template
    prompt_template_name = PromptTemplate.from_template(
        "I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
    )

    #chain = prompt_template_name | structured_llm
    chain = prompt_template_name | llm
    response = chain.invoke({"animal_type": animal_type, "pet_color": pet_color})
    return response

def langchain_agent():
    llm = ChatOllama(model="codellama", temperature=0.5)
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )
    print(result)

if __name__ == "__main__":
    langchain_agent()