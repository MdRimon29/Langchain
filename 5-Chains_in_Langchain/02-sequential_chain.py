from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGroq(
    model="llama-3.1-8b-instant"
)

prompt_1=PromptTemplate(
    template="Give me a medium length discussion on {topic}",
    input_variables=['topic']
)

prompt_2=PromptTemplate(
    template="Give me 2 poimts summary on \n {text}",
    input_variables=['text']
)

parser=StrOutputParser()

chain= prompt_1 | model | parser | prompt_2 | model | parser

result=chain.invoke({'topic': 'Natural beauty of Bangladesh'})

print(result)

chain.get_graph().print_ascii()