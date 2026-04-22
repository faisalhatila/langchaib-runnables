from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableSequence, RunnableParallel


load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="MiniMaxAI/MiniMax-M2.7",
#     task="text-generation"
# )
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)
# model = ChatOpenAI()


prompt1= PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=['topic']
)
prompt2= PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1 | model | parser),
    'linkedin': RunnableSequence(prompt2 | model | parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result)