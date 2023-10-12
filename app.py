import os
from datetime import datetime
from flask import Flask, render_template, request, redirect
import config


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config.upload_folder


@app.route("/")
def root():
    return render_template('index.html')


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True, use_reloader=True, threaded=True)
