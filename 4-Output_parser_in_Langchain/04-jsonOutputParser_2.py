from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model=ChatGroq(
    model="llama-3.1-8b-instant"
)

parser=JsonOutputParser()

template=PromptTemplate(    #It’s used to build prompts
    template= "give me 3 facts about {topic} \n {format_instruction}",  #This is the prompt structure.
    input_variables= ['topic'],
    partial_variables= {"format_instruction": parser.get_format_instructions()} #Partial variables are pre-filled values.
)

chain= template | model | parser

result= chain.invoke({'topic':'black hole'})

print(result)