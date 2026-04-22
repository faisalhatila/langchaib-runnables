# # Runnable lambda example: Convert any function into runnable

# from langchain_classic.schema.runnable import RunnableLambda

# def word_counter(text):
#     return len(text.split(' '))

# runnable_word_counter = RunnableLambda(word_counter)

# count = runnable_word_counter.invoke('Hi there, how are you?')

# print(count) 


from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

 
prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

def word_count(text):
    # return text.split()
    return len(text.split())

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

final_Chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_Chain.invoke({'topic':'India'})

formatted_result = """{} \n word count - {} """.format(result['joke'],result['word_count'])

print(formatted_result)