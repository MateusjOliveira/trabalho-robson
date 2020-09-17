#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
from flask_cors import CORS


# In[2]:


get_ipython().system('pip install flask-ngrok')
get_ipython().system('pip install flask-cors')


# In[7]:


from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
from flask_cors import CORS


# In[ ]:


app = Flask(__name__)

CORS(app)
run_with_ngrok(app)

@app.route('/')
def root():
    return "Server no ar"

@app.route('/api/v1/message', methods=['POST'])
def classify_post():

    value = request.json

    data = { "message" : value["message"]}

    response = jsonify(data)
    return response

@app.route('/api/v1/message', methods=['GET'])
def classify_get():

    value = request.args

    data = { "message" : value["message"]}
    
    response = jsonify(data)
    return response

#soma
@app.route('/soma/<v1>/<v2>', methods=['GET'])
def sum(v1,v2):

    value = request.args
    
    soma = { "Soma" : int(v1) + int(v2) }

    response = jsonify(soma)
    return response

app.run()


# In[ ]:




