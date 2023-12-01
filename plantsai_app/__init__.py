import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import plantsai_app.config as config
from plantsai_app.utils.plantsai import PlantsAI


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config.upload_folder
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

model = PlantsAI(weights_path=config.weights_path, thread=config.thread, image_size=config.image_size)


import plantsai_app.views