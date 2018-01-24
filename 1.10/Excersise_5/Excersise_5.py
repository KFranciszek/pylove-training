# -*- coding: utf-8 -*-
import os
from flask import Flask, request
encoding = "utf-8"

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Podaj nazwę pliku do odczytu, przykładowo: /file/hehe.txt'

@app.route("/file/<string:file_name>", methods=["GET"])
def get_file(file_name):
    try:
        with open(os.path.basename(file_name), "r", encoding=encoding) as plik:
            data = plik.read()
    except FileNotFoundError:
        data = 'Nie znaleziono pliku o podanej nazwie'
    return data

app.run(debug=True)