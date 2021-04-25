from fastapi import FastAPI
from pydantic import BaseModel

from src.datapipeline import DataPipeline
from src.model import Model
from src.db import Database

app = FastAPI()


class UrlItem(BaseModel):
    url: str


class EntityItem(BaseModel):
    entity: str


blacklist = ["style", "script", "head", "title", "meta", "[document]", "aside"]
db_file = "test.db"

datapipeline = DataPipeline(blacklist)
model = Model()
db = Database(db_file)
#db.create_table()


@app.post("/extract_entities")
def extract_entities(item: UrlItem):
    url = item.url
    text_body = datapipeline(url)
    results = model.predict(text_body)
    db.persist_to_db(url, results)

    entities = set([row[0] for row in results])
    return {"entities": list(entities)}


@app.get("/query_all_entities")
def query_entities():
    entities = db.get_entities()
    return {"entities": entities}


@app.post("/query_sentences")
def query_sentences(item: EntityItem):
    sentences = db.get_sentence_with_entity(item.entity)

    return {"sentences": sentences}
