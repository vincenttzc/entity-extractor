import sqlite3
import pickle


class Database:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()

        # create table if dont exist
        cur.execute("DROP TABLE entities")  # remove
        cur.execute("CREATE TABLE entities (url text, entity text, sentence text)")

        con.commit()
        con.close()

    def persist_to_db(self, url, data):
        data = [[url] + row for row in data]
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.executemany("INSERT INTO entities values (?, ?, ?)", data)
        con.commit()
        con.close()

    def get_entities(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()
        entities = cur.execute("SELECT DISTINCT entity FROM entities").fetchall()
        entities = [row[0] for row in entities]
        con.commit()
        con.close()

        return entities

    def get_sentence_with_entity(self, entity):
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


if __name__ == "__main__":
    db_file = "test.db"
    url = "https://en.wikipedia.org/wiki/GIC_(Singaporean_sovereign_wealth_fund)"
    with open("test_result.txt", "rb") as file:
        data = pickle.load(file)

    db = Database(db_file)
    db.create_table()
    db.persist_to_db(url, data)
    print(len(db.get_entities()))
    print(db.get_sentence_with_entity("Indonesia"))
