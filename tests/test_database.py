import sqlite3

from src.database import Database, DatabaseType, SqliteDB

db_file = "mydatabase.db"


def test_sqllitedb_class():
    """Test if SqliteDB is of the right class"""
    assert isinstance(
        SqliteDB(db_file), DatabaseType
    ), "SqliteDB is not a DatabaseType class"


def test_sqlitedb_create_table():
    """Test if SqliteDB can create table successfully"""
    # Drop table if exist
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS entities").fetchall()
    con.commit()
    con.close()

    # Create table
    sqlitedb = Database(SqliteDB(db_file))
    sqlitedb.create_table()

    # Test if table exsists
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    table_info = cur.execute(
        "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='entities'"
    ).fetchall()
    con.commit()
    con.close()

    assert table_info[0][0] == 1, "table is not created"


def test_sqlitedb_insert():
    """Test if SqliteDB can insert data into table successfully"""

    insert_row = [
        ["www.google.com", "google", "this is sentence 1"],
        ["www.google.com", "google_cloud", "this is sentence 2"],
    ]

    # Create table
    sqlitedb = Database(SqliteDB(db_file))
    sqlitedb.insert_into_db(insert_row)

    # Test if table exsists
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    table_info = cur.execute("SELECT count(*) FROM entities").fetchall()
    con.commit()
    con.close()

    assert table_info[0][0] == 2, "data is not inserted into table"


def test_sqlitedb_get_entities():
    """Test if SqliteDB can query for entities successfully"""
    # Query entities
    sqlitedb = Database(SqliteDB(db_file))
    entities = sqlitedb.get_entities()

    assert len(entities) == 2, "number of entities queried is not equal to 2"


def test_sqlitedb_get_sentences():
    """Test if SqliteDB can query for sentences with entities successfully"""
    # Query sentence with entity specified
    sqlitedb = Database(SqliteDB(db_file))
    entities = sqlitedb.get_sentences("google")

    assert len(entities) == 1, "number of sentence with 'google' entity is not 1"
