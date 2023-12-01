import json
from io import BytesIO
import numpy as np
from PIL import Image
from datetime import datetime
from flask import render_template, request, redirect, flash, url_for
from plantsai_app import config
from plantsai_app.models.plant import Plant, AddForm, DelForm
from plantsai_app import app, db, model
from plantsai_app.utils.functions import allowed_file


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, 
        # the browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash('Invalid file extension')
            return redirect(request.url)

        image_stream = BytesIO(file.read())
        image = np.array(Image.open(image_stream))
        result = model(image)  # predict on an image
        class_name = config.classes_names[result]
        return json.dumps({'class_name': class_name, 'class_id': result}, default=str)


@app.route("/result/<id>")
def result(id):
    plant = Plant.query.get(id)
    return render_template('result.html', plant=plant)


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        water = form.water.data
        new_plant = Plant(name, water)
        db.session.add(new_plant)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)


@app.route('/list')
def list_pup():
    plants = Plant.query.all()
    return render_template('list.html', plants=plants)
