from flask import Flask, json
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
    
    return json.dumps(hng_response, sort_keys= False)


if __name__ == "__main__": 
    app.run(debug=True)

