from abc import ABC, abstractmethod


class SourceType(ABC):
    """Base class of SourceType. Inherited class needs to have a
    extract_data method"""

    @abstractmethod
    def extract_data(self, input_link: str) -> str:
        """Extract text data from input_link and return as str

        Args:
            input_link (str): path or url

        Returns:
            str: text data from input_link
        """
        pass