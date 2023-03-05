# pylint: disable=import-error, missing-module-docstring
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mongodb_config import mongo_db_config
from pymongo import MongoClient


app = FastAPI()
client = MongoClient(mongo_db_config.get('DB_URI'))

app.add_middleware(
    CORSMiddleware,
    allow_origins='*', # This will need to be changed when we go live baby!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# print(client.server_info())

@app.get("/v1/api/")
async def main_page():
    """
    Date that will be displayed on the main page
    """
    return {"initial_message": "Welcome to the Home Page!"}

@app.get("/v1/api/black-series/get-all")
def get_all():
    """
    Get everything
    """
    pass
