import os
from flask import Flask, request, jsonify
from config import *
from translate import Translator

app = Flask(__name__)
translator = Translator()

app.config["DEBUG"] = True 

@app.route('/', methods=["GET"])
def available():
    support = "/supported_languages"
    translate = "/translate"
    return jsonify({"supported languages - GET": support, "translate - POST": translate})

@app.route('/supported_languages', methods=["GET"])
def get_supported():
    languages = translator.supported_languages()
    return jsonify({"supported languages": languages})


# @app.route('/supported_languages', methods=["GET"])


@app.route('/translate', methods=["POST"])
def get_prediction():
    source = request.json['source']
    target = request.json['target']
    text = request.json['text']
    translation = translator.translate(source, target, text)
    return jsonify({"output":translation})

app.run(host="0.0.0.0", port= 5000)
