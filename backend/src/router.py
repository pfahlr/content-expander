# backend/router.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from llm_client import generate_outputs
#import database

router = APIRouter()

class BasicRequest():
    q: str

class RepasteRequest(BaseModel):
    title: str
    content: str
    outputs: list[str]  # [twitter, youtube, instagram]

@router.post("/repaste")
def repaste(request: RepasteRequest):
    try:
        #result = generate_outputs(request.title, request.content, request.outputs)
        result = request
        return {'outputs': result}
    except Exception as e:
        raise HTTPException(500, str(e))


@router.get("/proof")
def proofoflife(request: BasicRequest ):
    try:
        print("wtf")
        result['status'] = 'alive'
        result['code'] = 200
        return {outputs: result}
    except Exception as e: 
        raise HTTPException(500, str(e))
