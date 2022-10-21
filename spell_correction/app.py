from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from spell_checker import correct_spell

app = FastAPI()

class Input(BaseModel):
    text: str


@app.get("/")
def health():
    return JSONResponse(content={"Server status": "Healthy"})


@app.post("/spell-check")
def spell_checker(inp: Input):
    content={"text": correct_spell(inp.text)}
    return JSONResponse(content=content)
