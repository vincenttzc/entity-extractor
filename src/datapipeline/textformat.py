from abc import ABC, abstractmethod


class TextFormat(ABC):
    """Base class of TextFormat. Inherited class needs to have a
    process_data method"""

    @abstractmethod
    def process_data(self, input_text: str) -> str:
        """Clean and process input_text so it can be fed into NER model

        Args:
            input_text (str): input text

        Returns:
            str: cleaned and processed text data
        """
        pass