import sqlite3
from typing import List

from src.database.databasetype import DatabaseType


class SqliteDB(DatabaseType):
    """Class to create table, insert data and query data from sqlite database

    Args:
        db (str): path to database file
    """

    def __init__(self, db: str):
        """Constructor method"""
        self.db = db

    def create_table(self):
        """Create entities table"""
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE entities (input_link text, entity text, sentence text)"
        )
        con.commit()
        con.close()

    def insert_into_db(self, data: List[List]):
        """Insert data into database. Elements of sublist need to match order in table

        Args:
            data (List[List]): Data to insert
        """
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.executemany("INSERT INTO entities values (?, ?, ?)", data)
        con.commit()
        con.close()

    def get_entities(self) -> List[str]:
        """Query all unique entities from database

        Returns:
            List[str]: list of unique entities
        """
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        entities = cur.execute("SELECT DISTINCT entity FROM entities").fetchall()
        entities = [row[0] for row in entities]
        con.commit()
        con.close()

        return entities

    def get_sentences(self, entity: str) -> List[str]:
        """Get sentences from database with the entity

        Args:
            entity (str): entity to query for sentences

        Returns:
            List[str]: list of sentences with the entity
        """
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        sentences = cur.execute(
            "SELECT sentence FROM entities WHERE entity=:ent", {"ent": entity}
        ).fetchall()
        con.commit()
        con.close()

        if len(sentences) > 0:
            sentences = [row[0] for row in sentences]

        return sentences