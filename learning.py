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