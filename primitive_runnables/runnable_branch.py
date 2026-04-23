from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch


load_dotenv()


prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)
# model = ChatOpenAI()

parser = StrOutputParser()

# report_gen_chain = RunnableSequence(prompt1, model, parser)
report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = report_gen_chain | branch_chain

result = final_chain.invoke({'topic':'USA vs IRAN war'})

formatted_result = """{} \n word count - {} """.format(result,len(result.split()))

print(formatted_result)