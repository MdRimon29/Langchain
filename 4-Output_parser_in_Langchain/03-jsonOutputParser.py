from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model=ChatGroq(
    model="llama-3.1-8b-instant"
)

parser=JsonOutputParser()

template=PromptTemplate(
    template= "give me 3 facts about {topic} \n {format_instruction}",
    input_variables= ['topic'],
    partial_variables= {"format_instruction": parser.get_format_instructions()}
)

prompt=template.format(topic= 'Philosophy') #filling the prompt template with the variable, returns a plain string

result=model.invoke(prompt) # returns AIMessage or similar

result2=parser.parse(result.content)    # Parse JSON

print(result2)

print(prompt)