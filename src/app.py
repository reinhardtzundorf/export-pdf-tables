# wsgi.py

from flask import Flask, request
from pathlib import Path

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
    # file_pdf = request.form.get("file_pdf")
    dry_run = request.form.get("dry_run")

    return f'file_name: {file_name}<br>dry_run: {dry_run}<br>file_type: {file_type}<br>'
