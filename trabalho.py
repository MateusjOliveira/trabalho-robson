#!/usr/bin/env python
# coding: utf-8

# In[6]:


from flask import Flask, jsonify
from flask_cors import CORS
from math import sqrt
import os


# In[ ]:


app = Flask(__name__)

CORS(app)

@app.route('/')
def root():
    return "Server no ar<br>"+\
           "https://trabalho-robson-mateus-n120029.herokuapp.com/soma/v1/v2<br>"+\
           "https://trabalho-robson-mateus-n120029.herokuapp.com/subt/v1/v2<br>"+\
           "https://trabalho-robson-mateus-n120029.herokuapp.com/div/v1/v2<br>"+\
           "https://trabalho-robson-mateus-n120029.herokuapp.com/mult/v1/v2<br>"+\
           "https://trabalho-robson-mateus-n120029.herokuapp.com/raiz/v1<br>"+\ 
           "https://trabalho-robson-mateus-n120029.herokuapp.com/pot/v1/v2<br>"+\ 
           "https://trabalho-robson-mateus-n120029.herokuapp.com/medari/v1/v2<br>"+\
           "https://trabalho-robson-mateus-n120029.herokuapp.com/medh/v1/v2<br>"+\
           "https://trabalho-robson-mateus-n120029.herokuapp.com/moda/v1/v2/v3<br>" 
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

    div = { "Divisão " : vlr1 / vlr2 }

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

    mult = { "Multiplicacao" : vlr1 * vlr2 }

    response = jsonify(mult)
    return response

#Raiz Quadrada
@app.route('/raiz/<v1>', methods=['GET'])
def raiz(v1):
    
    try: 
        vlr1 = int(v1)
    except:
        return "Valor errado"
    
    raiz = { "Raiz" : sqrt(vlr1)}

    response = jsonify(raiz)
    return response

#Potência
@app.route('/pot/<v1>/<v2>', methods=['GET'])
def pot(v1,v2):
    
    try: 
        vlr1 = int(v1)
    except:
        return "Valor errado"
    try: 
        vlr2 = int(v2)
    except:
        return "Valor errado"

    pote = { "Potencia" : vlr1 ** vlr2 }

    response = jsonify(pote)
    return response

#Média Aritmética
@app.route('/medari/<v1>/<v2>', methods=['GET'])
def meda(v1,v2):
    
    try: 
        vlr1 = int(v1)
    except:
        return "Valor errado"
    try: 
        vlr2 = int(v2)
    except:
        return "Valor errado"

    meda = { "Media Aritmetica " : (vlr1 + vlr2)/2 }

    response = jsonify(meda)
    return response

#Média Harmônica
@app.route('/medh/<v1>/<v2>', methods=['GET'])
def medh(v1,v2):
    
    try: 
        vlr1 = int(v1)
    except:
        return "Valor errado"
    try: 
        vlr2 = int(v2)
    except:
        return "Valor errado"

    medh = { "Media Harmonica " : 2/((1/vlr1) + (1/vlr2)) }

    response = jsonify(medh)
    return response

#Moda
@app.route('/moda/<v1>/<v2>/<v3>', methods=['GET'])
def mod(v1,v2,v3):
    
    try: 
        vlr1 = int(v1)
    except:
        return "Valor errado"
    try: 
        vlr2 = int(v2)
    except:
        return "Valor errado"
    try: 
        vlr3 = int(v3)
    except:
        return "Valor errado"
                                   
    if   vlr1 == vlr2 :
      moda = {"moda" : vlr1}
    elif vlr2 == vlr3 :
      moda = {"moda" : vlr2}
    elif vlr2 == vlr3 :
      moda = {"moda" : vlr3}    
    else :
     moda = { "Moda " : [vlr1,vlr2,vlr3] }

    response = jsonify(moda)
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

