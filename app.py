from flask import Flask, json, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    hng_response = {
        "slackUsername": "rabo", 
        "backend": True,
        "age": 28, 
        "bio": " Technical writter"
    }
    
    test= "this is just a test"
    
    data = json.dumps(hng_response, sort_keys=False)
    
    return Response(data, mimetype='application/json')


if __name__ == "__main__": 
    app.run(debug=True)

