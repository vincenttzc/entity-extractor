import sqlite3

from fastapi import FastAPI
from pydantic import BaseModel
from omegaconf import OmegaConf

from src.datasource import DataSource, WebSourceType
from src.datapipeline import DataPipeline, HTMLTextFormat
from src.database import Database, SqliteDB
from src.model import Model

app = FastAPI()

conf = OmegaConf.load("src/config/config.yaml")
database_file = conf["database_file"]
datasource_type = conf["datasource_type"]
text_format = conf["text_format"]
text_format_params = conf[text_format + "_params"]
database_type = conf["database_type"]

# Add new conditions if there are new types
if datasource_type == "web_source":
    datasource = DataSource(WebSourceType())

if text_format == "html":
    datapipeline = DataPipeline(HTMLTextFormat(**text_format_params))

if database_type == "sqlite":
    database = Database(SqliteDB(database_file))

model = Model()


class InputItem(BaseModel):
    input_link: str


class EntityItem(BaseModel):
    entity: str


@app.post("/extract_entities")
def extract_entities(item: InputItem):
    input_link = item.input_link
    raw_text = datasource.extract_data(input_link)
    text_body = datapipeline.process_data(raw_text)
    results = model.predict(text_body)
    results_with_input_link = [[input_link] + row for row in results]
    database.insert_into_db(results_with_input_link)

    con = sqlite3.connect(database_file)
    cur = con.cursor()
    entities = cur.execute("SELECT entity FROM entities").fetchall()
    con.commit()
    con.close()
    entities = [row[0] for row in entities]
    return {"entities": entities}


@app.get("/query_all_entities")
def query_entities():
    entities = database.get_entities()
    return {"entities": entities}


@app.post("/query_sentences")
def query_sentences(item: EntityItem):
    sentences = database.get_sentences(item.entity)

    return {"sentences": sentences}
