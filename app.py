import os
import json
from io import BytesIO
import numpy as np
from PIL import Image
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, flash, url_for
from plantsai import PlantsAI
import config


UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config.upload_folder
model = PlantsAI(weights_path=config.weights_path, thread=config.thread, image_size=config.image_size)


@app.route("/")
def root():
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            image_stream = BytesIO(file.read())
            image = np.array(Image.open(image_stream))
            result = model(image)  # predict on an image
            class_name = config.classes_names[result]
            print(result)
            return json.dumps({
                'class_name': class_name,
                'class_id': result
            }, default=str)
            # return redirect(url_for('result'))


@app.route("/result")
def result():
    return render_template('result.html')


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(host='localhost')
