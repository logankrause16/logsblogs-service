# pylint: disable=import-error, missing-module-docstring
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*', # This will need to be changed when we go live baby!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/v1/api/")
async def root():
    return {"initial_message": "Welcome to the Home Page!"}
