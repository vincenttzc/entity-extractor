from src.db import Database

db_file = "test.db"
db = Database(db_file)
db.create_table()
