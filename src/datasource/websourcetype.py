import requests

from src.datasource import SourceType


class WebSourceType(SourceType):
    """Class to create object that extracts data from web"""

    def extract_data(self, input_link: str) -> str:
        """Extracts html given url

        Args:
            input_link (str): url

        Returns:
            str: html text from url
        """
        html_content = requests.get(input_link).text

        return html_content