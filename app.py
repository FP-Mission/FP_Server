import flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy




app = flask.Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)

import models
db.create_all()

@app.route('/')
def get():
    return flask.send_from_directory("static", "map.html")


import resources
api.add_resource(resources.Gps, '/gps')
