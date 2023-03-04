# pylint: disable=import-error, missing-module-docstring
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
from schematics.models import Model
import settings
from pymongo import MongoClient


# class Comics(Model):
#     comic_id= ObjectId()

app = FastAPI()

client = MongoClient(settings.mongodb_uri)

app.add_middleware(
    CORSMiddleware,
    allow_origins='*', # This will need to be changed when we go live baby!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
