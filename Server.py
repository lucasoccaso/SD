#coding: utf-8

'''
    python 3.7.0
    CloudBroker Servidor
    Nome: Lucas Alexandre Occaso          RA: 620505
    Nome: Vitor Pratalli Camilo           RA: 620181

'''

import time
import os
from flask import Flask, request, redirect, url_for, current_app, send_from_directory
from werkzeug.utils import secure_filename



app = Flask(__name__)


@app.route('/Divulga', methods=['GET', 'POST'])
def Divulga():
    
    return 'Dados do provedor divulgados'


@app.route('/Consulta', methods=['GET', 'POST'])
def Consulta():

    return '1'
