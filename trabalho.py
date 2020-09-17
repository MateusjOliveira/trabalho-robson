#!/usr/bin/env python
# coding: utf-8

# In[6]:


from flask import Flask, jsonify
from flask_cors import CORS
import os


# In[ ]:


app = Flask(__name__)

CORS(app)

@app.route('/')
def root():
    return "Server no ar<br>"+
           "https://trabalho-robson-mateus-n120029.herokuapp.com/soma/<v1>/<v2>"

#soma
@app.route('/soma/<v1>/<v2>', methods=['GET'])
def sum(v1,v2):
    
    soma = { "Soma" : int(v1) + int(v2) }

    response = jsonify(soma)
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

