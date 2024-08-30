from langchain_community.document_loaders import YoutubeLoader
from langchain. text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models.ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.ollama.llms import Ollama

embeddings = OllamaEmbeddings(model="gemma:2b")
video_url = "https://www.youtube.com/watch?v=yXpgqAWWUrs"

def create_vector_db_from_youtube_url(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db

def get_response_from_query(db, query, k=4):
    # gemma 2b can handle 2048~4096 tokens
    docs = db.similarity_search(query, k=k)
    docs_page_content = "".join([d.page_content for d in docs])

    llm = Ollama(model="gemma:2b")

    prompt = PromptTemplate(
            input_variables=["question", "docs"]
            template="""
            You are a helpful YouTube assistant that can answer questions about videos based on the video's transcript.
            Answer the following question: {question}
            By searching the following video transcript: {docs}
            Only use the factual information from the transcript to answer the question.
            If you feel like you don't have enough information to answer the question, say 'I don't know'
            Your answers should be detailed.
            """
            )
    chain = prompt | llm
    response = chain.run(question=query, docs=docs_page_content)
    response = response.replace("\n", "")
    return response
            

print(create_vector_db_from_youtube_url(video_url))
