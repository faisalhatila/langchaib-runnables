import random
from abc import ABC, abstractmethod

class Runnable(ABC):

    @abstractmethod
    def invoke(input_data):
        pass

class FakeLLM(Runnable):
    def __init__(self):
        print('LLM created')

    def invoke(self, prompt):

        response_list = [
            'Islamabad is the capital of Pakistan',
            'PSL is a cricket league',
            'AI stands for Artificial Intelligience'
        ]

        return {'response': random.choice(response_list)}
    
    def predict(self, prompt):

        response_list = [
            'Islamabad is the capital of Pakistan',
            'PSL is a cricket league',
            'AI stands for Artificial Intelligience'
        ]

        return {'response': random.choice(response_list)}

class FakePromptTemplate(Runnable):

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
    
    def invoke(self,input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)
    
class RunnableConnector(Runnable):
    
    def __init__(self, runnable_list):
        self.runnable_list=runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            runnable.invoke(input_data)