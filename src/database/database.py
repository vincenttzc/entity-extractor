from abc import ABC, abstractmethod
from typing import List

from src.database.databasetype import DatabaseType


class Database:
    """Create Database object based on database_type specified

    Args:
        database_type (DatabaseType): Inherited DatabaseType class

    Raises:
        ValueError: raises error when text_format is not a DatabaseType class
    """

    def __init__(self, database_type: DatabaseType):
        """Constructor method"""
        if isinstance(database_type, DatabaseType):
            self.database_type = database_type
        else:
            raise ValueError(
                "database_type needs to inherit from " + DatabaseType.__name__
            )

    def create_table(self):
        """Create table in database"""
        self.database_type.create_table()

    def insert_into_db(self, data: List[List]):
        """Insert data into database table

        Args:
            data (List[List]): data to insert into database table
        """
        self.database_type.insert_into_db(data)

    def get_entities(self) -> List[str]:
        """Query all unique entities

        Returns:
            List[str]: list of entities
        """
        return self.database_type.get_entities()

    def get_sentences(self, entity: str) -> List[str]:
        """Query for sentences containing entity from database

        Args:
            entity (str): entity to query for sentence

        Returns:
            List[str]: list of sentences containing entity
        """
        return self.database_type.get_sentences(entity)
