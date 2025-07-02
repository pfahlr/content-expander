# backend/router.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from llm_client import generate_outputs

router = APIRouter()

class RepasteRequest(BaseModel):
    title: str
    content: str
    outputs: list[str]  # [twitter, youtube, instagram]

@router.post("/repaste")
def repaste(request: RepasteRequest):
    try:
        result = generate_outputs(request.title, request.content, request.outputs)
        return {outputs: result}
    except Exception as e:
        raise HTTPException(500, str(e))


@router.get("/proofoflife")
def proofoflife(request: RepasteRequest):
    try:
        result = {'status':'alive', 'code':'200'}
        return {outputs:result}
    except Exception as e:
        raise HTTPException(500, str(e))
