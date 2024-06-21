# streamlit run flask_api.py

from flask import Flask, request, jsonify
import streamlit as st
from threading import Thread
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    # st.write("This is a Streamlit app embedded in a Flask app.") <- this will cause "missing ScriptRunContext" error
    return "hello 002"

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.json
    # Process the data (this is just an example)
    item = {
        "name": data.get("name"),
        "description": data.get("description"),
        "price": data.get("price"),
        "tax": data.get("tax")
    }
    return jsonify(item), 200

@app.route('/hello', methods=['GET'])
def hello():
    st.title("hello")
    item = {"text": "hello 001"}
    return jsonify(item), 200

def run_flask():
    app.run(port=5000)

# Run Flask app in a separate thread
flask_thread = Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

st.title("Streamlit with Flask API Example 002")


