#coding: utf-8

'''
    python 3.7.0
    CloudBroker Servidor
    Nome: Lucas Alexandre Occaso          RA: 620505
    Nome: Vitor Pratalli Camilo           RA: 620181

'''

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from pprint import pprint
import json
import bson



app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://admin:admin123@ds117545.mlab.com:17545/db_cloudbroker"
mongo = PyMongo(app)


@app.route('/Divulga', methods=['GET', 'POST'])
def Divulga():
    data = request.get_json()
    print (data)
    mongo.db['provedores'].insert_one(
        {
            'provedor_id': data['provedor_id'],
            'vcpu': data['vcpu'],
            'ram': data['ram'],
            'disco': data['disco'],
            'custo': data['custo'],  
            'vm': data['vm']
        })
    return 'Dados do provedor divulgados'


@app.route('/Consulta', methods=['GET', 'POST'])
def Consulta():
    data = request.get_json()
    busca = mongo.db['provedores'].find(
        {
            'vcpu':{'$gte': data['CPU']},
            'ram': {'$gte': data['RAM']},
            'disco': {'$gte': data['DISCO']}
        }
    )

    if busca['vm'] > 0:
        mongo.db['provedores'].update_one(
            {
                'provedor_id': busca['provedor_id']
            }, {'$set': {'vm': busca['vm']-1}}
            
        )
        return busca['provedor_id']
    else:
        return 'indisponivel'

@app.route('/Libera', methods=['GET', 'POST'])
def Libera():
    data = request.get_json()
    mongo.db['provedores'].update_one(
            {
                'provedor_id': data['provedor_id']
            }, {'$set': {'vm': busca['vm']+1}}
        )
