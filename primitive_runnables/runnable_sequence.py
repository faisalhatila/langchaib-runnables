## String output Sequence

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
# from dotenv import load_dotenv
# from langchain_classic.schema.runnable import RunnableSequence


# load_dotenv()

# prompt1 = PromptTemplate(
#     template='Write a joke about {topic}',
#     input_variables=['topic']
# )

# model = ChatOpenAI()

# parser = StrOutputParser()

# prompt2 = PromptTemplate(
#     template='Explain the following joke - {text}',
#     input_variables=['text']
# )

# chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

# result = chain.invoke({'topic':'AI'})

# print(result)

## JSON Output Sequence

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the following joke: {joke}",
    input_variables=["joke"]
)

# Step 1: generate joke
joke_step = prompt1 | model | parser

# Step 2: convert joke into dict (preserve it)
wrap_joke = RunnableLambda(lambda joke: {"joke": joke})

# Step 3: generate explanation but KEEP joke
def add_explanation(data):
    explanation = (prompt2 | model | parser).invoke({"joke": data["joke"]})
    return {
        "joke": data["joke"],
        "explanation": explanation
    }

explain_step = RunnableLambda(add_explanation)

# Full sequence
chain = RunnableSequence(
    joke_step,
    wrap_joke,
    explain_step
)

result = chain.invoke({"topic": "AI"})
print(result)