import os
from pyexpat import model
import string
from urllib import response
import openai

openai.api_key = "GT3_API_KEY"

# response = openai.Completion.create(model="text-davinci-002", prompt="Say this is a test", temperature=0, max_tokens=6)

# print(response)

def createBlogText(words):
    # words = words.split()
    # words = string.join(', ', words)
    return openai.Completion.create(model="text-davinci-002",
                                    prompt="write a blog.\n\nWords: {words}",
                                    temperature=0,
                                    max_tokens=2019,
                                    top_p=1,
                                    best_of=2,
                                    frequency_penalty=0.2,
                                    presence_penalty=0)