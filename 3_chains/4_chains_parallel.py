from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_community.chat_models.ollama import ChatOllama
from langchain.schema.runnable import RunnableLambda, RunnableParallel

model = ChatOllama(model="gemma:2b", temperature=0.1)

messages = [
        ("system", "You are an expert product reviewer."),
        ("human", "List the main features of the product {product_name}.")
        ]
prompt_template = ChatPromptTemplate.from_messages(messages)

# Define pros
def analyze_pros(features):
    pros_template = ChatPromptTemplate.from_messages(
            [
                ("system", "You are an expert product reviewer."),
                ("human", "Given these features: {features}, list the pros of these features")
                ]
            )
    return pros_template.format_prompt(features=features)

# Define cons
def analyze_cons(features):
    cons_template = ChatPromptTemplate.from_messages(
            [
                ("system", "You are an expert product reviewer."),
                ("human", "Given these features: {features}, list the cons of these features")
                ]
            )
    return cons_template.format_prompt(features=features)

# Combine pros and cons
def combine_pros_cons(pros, cons):
    return f"Pros:\n{pros}\n\nCons:\n{cons}"

pros_branch_chain = (RunnableLambda(lambda x: analyze_pros(x)) | model | StrOutputParser())
cons_branch_chain = (RunnableLambda(lambda x: analyze_cons(x)) | model | StrOutputParser())

chain = (
        prompt_template
        | model
        | StrOutputParser()
        | RunnableParallel(branches={"pros": pros_branch_chain, "cons": cons_branch_chain})
        | RunnableLambda(lambda x: combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"]))
        )

response = chain.invoke({"product_name": "Smartphone"})
print(response)
