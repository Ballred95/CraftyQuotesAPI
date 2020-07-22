from flask import Flask, request, jsonify
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

class Save(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    imgsrc = db.Column(db.String(), unique=False)
    text_content = db.Column(db.String(100), unique=False)
    text_align = db.Column(db.String(100), unique=False)
    clipart = db.Column(db.String(100), unique=False)

    def __init__(self, name, imgsrc, text_content, text_align, clipart):
        self.name = name
        self.imgsrc = imgsrc
        self.text_content = text_content
        self.text_align = text_align
        self.clipart = clipart

class SaveSchema(ma.Schema):
    class Meta:
        fields = ('name', 'imgsrc', 'text_content', 'text-align', 'clipart')

save_schema = SaveSchema()
saves_schema = SaveSchema(many=True)

@app.route('/saved', methods=["POST"])
def add_save():
    name = request.json['name']
    imgsrc = request.json['imgsrc']
    text_content = request.json['text_content']
    text_align = request.json['text_align']
    clipart = request.json['clipart']

    new_save = Save(name, imgsrc, text_content, text_align, clipart)

    db.session.add(new_save)
    db.session.commit()

    save = Save.query.get(new_guide.id)


if __name__ == "__main__":
    app.debug = True
    app.run()




