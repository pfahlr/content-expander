from flask import Flask, request, jsonify, json
import random
import requests
app = Flask(__name__)


@app.route("/pol")
def proof_of_life():
  return jsonify({'response':'alive','code':200})

@app.route("/polhtml")
def proof_of_life_html():
  return "<html><head><title>welcome to flask backend thing</title><head><body><h1>Welcome to flask</h1></body></html>"



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)

