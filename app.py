from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
import io
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://muetowpioyxcga:eed6e5944d9c5a4ed3f71fbc213e3b5cd7414cccf5e44def565f557af88a618d@ec2-107-22-7-9.compute-1.amazonaws.com:5432/dab0oio12ag87f"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

heroku = Heroku(app)
CORS(app)
