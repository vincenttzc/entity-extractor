import sqlite3

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app import app


client = TestClient(app)

# Drop table if exist, then create table
db_file = "mydatabase.db"
con = sqlite3.connect(db_file)
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS entities")
cur.execute("CREATE TABLE entities (input_link text, entity text, sentence text)")
con.commit()
con.close()


def test_extract_entities():
    """Test if /extract_entities endpoint can make a successful post request and
    if response message is correct"""

    url = "https://en.wikipedia.org/wiki/Betta"
    response = client.post("/extract_entities", json={"input_link": url})

    assert response.status_code == 200, "status code not 200"
    assert list(response.json().keys()) == [
        "entities"
    ], "response json does not only have entities key"


def test_query_all_entities():
    """Test if /query_all_entities endpoint can make a successful get request and
    if response message is correct"""

    response = client.get("/query_all_entities")

    assert response.status_code == 200
    assert list(response.json().keys()) == [
        "entities"
    ], "response json does not only have entities key"


def test_query_sentences():
    """Test if /query_senteces endpoint can make a successful post request and
    if response message is correct"""

    response = client.post("/query_sentences", json={"entity": "betta"})

    assert response.status_code == 200
    assert list(response.json().keys()) == [
        "sentences"
    ], "response json does not only have sentences key"