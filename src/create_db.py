from omegaconf import OmegaConf

from src.database import Database, SqliteDB

conf = OmegaConf.load("../config/config.yaml")
database_file = conf["database_file"]
database_type = conf["database_type"]

if database_type == "sqlite":
    database = Database(SqliteDB(database_file))

database.create_table()