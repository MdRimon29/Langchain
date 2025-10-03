from langchain_community.document_loaders import TextLoader
from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

prompt = PromptTemplate(
    template='Write a 5 line of summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('7-Documents_loader_in_langchain/football.txt', encoding='utf-8')   # load the .txt file

docs = loader.load()

#print(docs)
print(type(docs))
print(len(docs))    #how many docs are there
#print(docs[0])  # there are two things are on a docs. One is page_content, another is metadata. Docs[0] extract the both.
print(type(docs[0]))
#print(docs[0].page_content) # this is how we can extract the page content

chain = prompt | llm | parser

print(chain.invoke({'poem': docs[0].page_content}))