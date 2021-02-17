import logging
import json
from .helpers.database import Database
import azure.functions as func

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
Database().connect(app=app)

db = SQLAlchemy(app)

class Testing(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    desc = db.Column(db.String(200))

class TestingA(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    desc = db.Column(db.String(200))

@app.route('/')
def hello_world():
    get_all = Testing.query.all()
    logging.info('[get_all] %s', len(get_all))
    logging.info('[get_all] %s', get_all[0].id)
    return 'Hello World!'

@app.route('/hi')
def hi():
    return 'Hi World!'

@app.route('/hello')
@app.route('/hello/<name>', methods=['POST', 'GET'])
def hello(name=None):
    return name != None and 'Hello, ' + name or 'Hello, '+request.args.get('name')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    get_all = Testing.query.all()
    logging.info('[get_all] %s', len(get_all))
    logging.info('[get_all] %s', get_all[0].id)
    uri=req.params['uri']

    with app.test_client() as c:
        # doAction = {
        #     "GET": c.get(uri).data,
        #     "POST": c.post(uri).data
        # }
        # resp = doAction.get(req.method).decode()
        resp = {
            'test': get_all[0].id,
            'success': True
        }
        return func.HttpResponse(json.dumps(resp))

    # return func.HttpResponse(json.dumps({
    #     'success': True,
    #     'data': 'good luck have fun'
    # }))
