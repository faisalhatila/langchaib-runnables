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
    
llm = FakeLLM()

print(llm.predict('What is the capital of Pakistan'))


class FakePromptTemplate:

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)
template = FakePromptTemplate(
    template='Write a poem about {topic}',
    input_variables=['topic']
)

print(template.format({'topic':'Pakistan'}))