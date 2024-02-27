from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/restapi', methods=['POST'])
def restapi():
    data = request.get_json()
    text = data['text']
    if text == "hi":
        result = "hello"
    else:
        result = "what?"
    file = {
        "result" : result,
    }
    return jsonify(file), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
