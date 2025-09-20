from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(
    model="llama-3.1-8b-instant"
)

chat_history=[
    SystemMessage(content='You are a helpful AI assistant')
] # here we store the context

while True:
    prompt= input("User: ")
    chat_history.append(HumanMessage(content=prompt))
    if prompt=="exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)