#coding: utf-8

'''
    python 3.7.0
    CloudBroker Servidor
    Nome: Lucas Alexandre Occaso          RA: 620505
    Nome: Vitor Pratalli Camilo           RA: 620181

'''

import time
import json
import os
from flask import Flask, request, redirect, url_for, current_app, send_from_directory
from werkzeug.utils import secure_filename
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


@app.route('/Divulga', methods=['GET', 'POST'])
def Divulga():
    provedor_info = request.form
    json_provedor = json.dumps(provedor_info)

    with open('db.txt', 'a') as arquivo:
        json.dump(json_provedor, arquivo)
    arquivo.close()

    return 'Dados do provedor divulgados'


@app.route('/Consulta', methods=['GET', 'POST'])
def Consulta():
    with open('db.txt', 'r') as arquivo:
        json_data = arquivo.read() 
    arquivo.close()

    print (json_data)

    return '1'
