import os
import openai
from flask import Flask, jsonify
from flask import make_response
from flask import request

from gtp3.createblog import createBlogText

# # Load your API key from an environment variable or secret management service
# openai.api_key = "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"

# response = openai.Completion.create(model="text-davinci-002", prompt="Say this is a test", temperature=0, max_tokens=6)

# print(response)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"


@app.route('/api/v1/createblog', methods=['GET'])
def get_blog():
    keywords = request.args.get('keywords')
    print(keywords)
    return createBlogText(keywords)

if __name__ == '__main__':
    app.run(debug=True) 