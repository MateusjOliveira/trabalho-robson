#!/usr/bin/env python
# coding: utf-8

# In[6]:


from flask import Flask, jsonify
from flask_cors import CORS
import os


# In[ ]:


app = Flask(__name__)

CORS(app)
#run_with_ngrok(app)

@app.route('/')
def root():
    return "Server no ar"

#soma
@app.route('/soma/<v1>/<v2>', methods=['GET'])
def sum(v1,v2):
    
    soma = { "Soma" : int(v1) + int(v2) }

    response = jsonify(soma)
    return response

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()

