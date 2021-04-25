from typing import List, Union

from bs4 import BeautifulSoup
from bs4.element import Comment, NavigableString, Script, Doctype

from src.datapipeline.textformat import TextFormat


class HTMLTextFormat(TextFormat):
    """Clean and process HTML text data for NER model

    Args:
        blacklist (List[str]): html tags to filter out when cleaning the html text data
    """

    def __init__(self, blacklist: List[str]):
        """Constructor method"""
        self.blacklist = blacklist

    def process_data(self, input_text: str) -> str:
        """Remove all HTML tags and filter text in self.blacklist HTML tags

        Args:
            input_text (str): HTML raw text

        Returns:
            str: text data with text in self.blacklist tags removed
        """
        soup = BeautifulSoup(input_text, "html.parser")
        texts = soup.findAll(text=True)
        visible_texts = filter(self._tag_visible, texts)

        return " ".join(t.strip() for t in visible_texts)

    def _tag_visible(
        self, element: Union[Doctype, NavigableString, Script, Comment]
    ) -> bool:
        """Private method to filter out tags in self.blacklist and Comment tags

        Args:
            element (Union[Doctype, NavigableString, Script, Comment]): [description]

        Returns:
            bool: True or False
        """
        if element.parent.name in self.blacklist:
            return False
        if isinstance(element, Comment):
            return False
        return True
