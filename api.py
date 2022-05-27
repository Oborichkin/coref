from coref import nlp
from fastapi import FastAPI
from typing import List, Union
from pydantic import BaseModel

app = FastAPI()



class TextModel(BaseModel):
    text: Union[str, List[str]]


@app.post("/")
def coreference_resolution(text_model: TextModel):
    if isinstance(text_model.text, str):
        return nlp(text_model.text)._.coref_resolved
    else:
        return [nlp(txt)._.coref_resolved for txt in text_model.text]
