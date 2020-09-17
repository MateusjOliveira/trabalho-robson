#!/usr/bin/env python
# coding: utf-8

# In[6]:


from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
from flask_cors import CORS
import os


# In[ ]:


app = Flask(__name__)

CORS(app)
run_with_ngrok(app)

@app.route('/')
def root():
    return "Server no ar"

#soma
@app.route('/soma/<v1>/<v2>', methods=['GET'])
def sum(v1,v2):
    
    value = request.json
    
    soma = { "Soma" : int(v1) + int(v2) }

    response = jsonify(soma)
    return response

app.run()

