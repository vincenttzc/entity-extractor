import requests
from abc import ABC, abstractmethod

from src.datasource.sourcetype import SourceType


class DataSource:
    """Class to extract text data from input_link depending on the source_type
    provided

    Args:
        source_type (SourceType): Inherited SourceType class

    Raises:
        ValueError: raises error when source_type is not a SourceType class
    """

    def __init__(self, source_type: SourceType):
        """[summary]"""
        if isinstance(source_type, SourceType):
            self.source_type = source_type
        else:
            raise ValueError("logger needs to inherit from " + SourceType.__name__)

    def extract_data(self, input_link):

        return self.source_type.extract_data(input_link)
