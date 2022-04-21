import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import VARCHAR

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__) # instantiate app
app.config.from_object("config.TestingConfig") # load testing config from config.py
db = SQLAlchemy() # instantiate sqlalchemy
db.init_app(app) # link sqlalchemy to app

# Example for a database model
class MyModel(db.Model):
    id = db.Column("id", VARCHAR, primary_key=True, unique=True, nullable=False)

# Example route
@app.route("/", methods=['GET'])
def get_value():
    mod = MyModel.query.first()
    return jsonify(mod.id), 200
