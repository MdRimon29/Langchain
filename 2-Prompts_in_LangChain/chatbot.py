from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(
    model="llama-3.1-8b-instant"
)

chat_history=[] # here we store the context

while True:
    prompt= input("User: ")
    chat_history.append(prompt)
    if prompt=="exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(result)
    print("AI: ",result.content)

print(chat_history)