from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_community.chat_models.ollama import ChatOllama


PROJECT_ID = "langchain-test-422ef"
SESSION_ID = "user_session_new"
COLLECTION_NAME = "chat_history"

# Initializing Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initializing firestore Chat Message History
print("Initializing firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
        session_id = SESSION_ID,
        collection = COLLECTION_NAME,
        client = client
        )
print("Chat history initialized.")
print(f"Current Chat History: {chat_history.messages}")

# Defining model
model = ChatOllama(model="gemma:2b", temperature=0.5)
print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)

    ai_response = model.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"Gemma: {ai_response.content}")
