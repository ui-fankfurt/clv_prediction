import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for, send_from_directory
import pickle
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from model import process_csv


ALLOWED_EXTENSIONS = set(['csv'])
# Makes sure the file uploaded is a csv file
def allowed_filenames(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def create_app():
    app = Flask(__name__)

    @app.route('/upload', methods = ['GET', "POST"])
    def upload():
        if request.method == 'POST':
            file = request.files['file']
            if file and allowed_filenames(file.filename):
                filename = secure_filename(file.filename)
                #new_filename = f"{filename.split('.')[0]}_{str(datetime.now())}.csv"
                new_filename = "online_retail_input.csv"
                save_location = f"input\{new_filename}"#os.path.join('input', new_filename)
                file.save(save_location)
                
                output_file = process_csv(save_location)

                return send_from_directory('output', output_file)


            return 'uploaded'
        return render_template('upload.html')
    
    return app