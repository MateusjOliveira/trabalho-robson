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
    return "Server no ar<br>"+           "https://trabalho-robson-mateus-n120029.herokuapp.com/soma/v1/v2<br>"+           "https://trabalho-robson-mateus-n120029.herokuapp.com/subt/v1/v2<br>"+           "https://trabalho-robson-mateus-n120029.herokuapp.com/div/v1/v2<br>"+           "https://trabalho-robson-mateus-n120029.herokuapp.com/mult/v1/v2<br>" 

#soma
@app.route('/soma/<v1>/<v2>', methods=['GET'])
def sum(v1,v2):
    
    try: 
        vlr1 = int(v1)
    except:
        return "Valor errado"
    try: 
        vlr2 = int(v2)
    except:
        return "Valor errado"

    soma = { "Soma" : vlr1 + vlr2}

    response = jsonify(soma)
    return response

#Subtrair
@app.route('/subt/<v1>/<v2>', methods=['GET'])
def subt(v1,v2):
    
    try: 
        vlr1 = int(v1)
    except:
        return "Valor errado"
    try: 
        vlr2 = int(v2)
    except:
        return "Valor errado"

    sub = { "Subtrair" : vlr1 - vlr2 }

    response = jsonify(sub)
    return response

#Dividir
@app.route('/div/<v1>/<v2>', methods=['GET'])
def divi(v1,v2):
    
    try: 
        vlr1 = int(v1)
    except:
        return "Valor errado"
    try: 
        vlr2 = int(v2)
    except:
        return "Valor errado"

    div = { "Soma" : vlr1 / vlr2 }

    response = jsonify(div)
    return response

#Multiplicar
@app.route('/mult/<v1>/<v2>', methods=['GET'])
def mult(v1,v2):
    
    try: 
        vlr1 = int(v1)
    except:
        return "Valor errado"
    try: 
        vlr2 = int(v2)
    except:
        return "Valor errado"

    mult = { "Soma" : vlr1 * vlr2 }

    response = jsonify(mult)
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

