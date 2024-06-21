from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route('/', methods=['GET'])
def root():
    return jsonify({"text": "hello"}), 200

if __name__ == "__main__":
    app.run(port=5000)
