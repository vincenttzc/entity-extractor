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
        """Constructor method"""
        if isinstance(source_type, SourceType):
            self.source_type = source_type
        else:
            raise ValueError("source_type needs to inherit from " + SourceType.__name__)

    def extract_data(self, input_link: str) -> str:
        """Extract text data from input_link

        Args:
            input_link (str): url or path to file

        Returns:
            str: text extracted from input_link
        """

        return self.source_type.extract_data(input_link)
