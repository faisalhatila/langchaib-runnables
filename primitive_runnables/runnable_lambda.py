# Runnable lambda example: Convert any function into runnable

from langchain_classic.schema.runnable import RunnableLambda

def word_counter(text):
    return len(text.split(' '))

runnable_word_counter = RunnableLambda(word_counter)

count = runnable_word_counter.invoke('Hi there, how are you?')

print(count)