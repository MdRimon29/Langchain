from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model=ChatGroq(
    model="llama-3.1-8b-instant"
)

schema = [
    ResponseSchema(name="Fact-1",description="Fact-1 about the topic"),
    ResponseSchema(name="Fact-2",description="Fact-2 about the topic"),
    ResponseSchema(name="Fact-3",description="Fact-3 about the topic")
]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(    #It’s used to build prompts
    template= "give me 3 facts about {topic} \n {format_instruction}",  #This is the prompt structure.
    input_variables= ['topic'],
    partial_variables= {"format_instruction": parser.get_format_instructions()} #Partial variables are pre-filled values.
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)