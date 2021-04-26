from src.datapipeline.textformat import TextFormat


class DataPipeline:
    """Class to clean and process text data given the text_format

    Args:
        text_format (TextFormat): Inherited TextFormat class

    Raises:
        ValueError: raises error when text_format is not a TextFormat class
    """

    def __init__(self, text_format: TextFormat):
        """Constructor method"""
        if isinstance(text_format, TextFormat):
            self.text_format = text_format
        else:
            raise ValueError("text_format needs to inherit from " + TextFormat.__name__)

    def process_data(self, input_text: str) -> str:
        """Clean and process input_text given the text_format

        Args:
            input_text (str): input text in the text_format specified

        Returns:
            str: cleaned and processed text data
        """
        return self.text_format.process_data(input_text)