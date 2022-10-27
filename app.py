from pstats import SortKey
from flask import Flask, json

app = Flask(__name__)

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
