import json
# pylint: disable=import-error
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient



app = Flask(__name__)
CORS(app, support_credentials=False)
client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos


@app.route("/v1/api/")
def home():
    """Return the initial home page data
    """
    data = { "initial_message": "Hello World!"}
    return_data = json.dumps(data)
    return return_data

@app.route("/v1/api/black-series-scrapper")
def scrape_page():
    """Scrape the black series goodies
    """
    return "WIP"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
