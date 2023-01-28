from os import getenv
from fastapi import FastAPI, Request, Response
import http
import json


app = FastAPI()

@app.post("/webhook", status_code=http.HTTPStatus.ACCEPTED)
async def webhook(request: Request):
    return json.dumps(request)


@app.get("/", status_code=http.HTTPStatus.ACCEPTED)
async def home(request: Request):
    return json.dumps('hey')
