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
template = FakePromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length','topic']
)

prompt = template.format({'length':'short','topic':'Pakistan'})

llm = FakeLLM()

result = llm.predict(prompt)

# print(llm.predict('What is the capital of Pakistan'))
print(result)