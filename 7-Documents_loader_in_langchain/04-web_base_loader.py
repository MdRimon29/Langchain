from langchain_community.document_loaders import WebBaseLoader
from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm=ChatGroq(
    model="llama-3.1-8b-instant"
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text. \n {text}',
    input_variables=['question','text']
)


loader = WebBaseLoader('https://python.langchain.com/docs/how_to/document_loader_web/')

docs = loader.load()

chain = prompt | llm | parser

print(chain.invoke({'question':'What is the topic name in this page?', 'text':docs[0].page_content}))