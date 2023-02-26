import json
# pylint: disable=import-error
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=False)


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
