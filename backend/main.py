from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from parser import calculate

app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_methods=['*'],allow_headers=['*'])

class Req(BaseModel):
    expression:str

@app.post('/calculate')
def calc(req:Req):
    try:
        return {'result': calculate(req.expression)}
    except Exception as e:
        return {'error': str(e)}