import requests

from src.datapipeline import DataPipeline, TextFormat, HTMLTextFormat


def test_htmltextformat_class():
    """Test if HTMLTextFormat is of the correct class"""
    blacklist = ["style", "script", "head", "title", "meta", "[document]", "aside"]
    assert isinstance(
        HTMLTextFormat(blacklist), TextFormat
    ), "HTMLTextFormat is not a TextFormat class"


def test_htmltextformat_process_data():
    """Test if HTMLTextFormat can successfully process and clean HTML text"""
    url = "https://en.wikipedia.org/wiki/Betta"
    html = requests.get(url).text
    blacklist = ["style", "script", "head", "title", "meta", "[document]", "aside"]

    html_datapipeline = DataPipeline(HTMLTextFormat(blacklist))
    processed_text = html_datapipeline.process_data(html)

    assert (
        "<!doctype html>" not in processed_text
    ), "HTML text not cleaned and processed. HTML tags still exist"