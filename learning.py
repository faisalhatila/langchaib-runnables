import random

class FakeLLM:
    def __init__(self):
        print('LLM created')
    
    def predict(self, prompt):

        response_list = [
            'Islamabad is the capital of Pakistan',
            'PSL is a cricket league',
            'AI stands for Artificial Intelligience'
        ]

        return {'response': random.choice(response_list)}

class FakePromptTemplate:

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)


class FakeLLMChain:
    def __init__(self,llm, prompt):
        self.llm = llm
        self.prompt = prompt
    
    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result['response']
    

template = FakePromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length','topic']
)

llm = FakeLLM()

chain = FakeLLMChain(llm, template)

result = chain.run({'length':'short','topic':'Pakistan'})

# prompt = template.format({'length':'short','topic':'Pakistan'})


# result = llm.predict(prompt)

# print(llm.predict('What is the capital of Pakistan'))
print(result)
