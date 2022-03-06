# wsgi.py

from flask import Flask, request
from pathlib import Path
import requests


app = Flask(__name__,
            static_url_path='/assets', 
            static_folder='assets',
            template_folder='templates')


@app.route("/", methods=["GET"])
def form_example():
    return open('src/templates/index.html').read()


@app.route("/", methods=["POST"])
def extract_pdf_tables():
    file_name = request.form.get("file_name")
    file_type = request.form.get("file_type")
    dry_run = request.form.get("dry_run")
    
    # Upload file.
    uploaded_file = upload_file()

    return f'upload_file_name{uploaded_file}'
    # return f'file_name: {file_name}<br>dry_run: {dry_run}<br>file_type: {file_type}<br>'


def upload_file():
   if request.method == 'POST':
      f = request.files['file_pdf']
      f.save(f'uploads/{f.filename}')
      return f.filename
