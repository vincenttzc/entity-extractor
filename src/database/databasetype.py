from abc import ABC, abstractmethod
from typing import List


class DatabaseType(ABC):
    """Base class of DatabaseType. Inherited class needs to contain the following methods"""

    @abstractmethod
    def create_table(self):
        """Create table in database"""
        pass

    @abstractmethod
    def insert_into_db(self, data: List[List]):
        """Insert data into database table

        Args:
            data (List[List]): data to insert into database table
        """
        pass