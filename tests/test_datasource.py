from src.datasource import DataSource, SourceType, WebSourceType


def test_websourcetype_class():
    """Test if WebSourceType is of the right class"""
    assert isinstance(
        WebSourceType(), SourceType
    ), "WebSourceType is not a SourceType class"


def test_websourcetype_extract_data():
    """Test if WebSourceType can successfully extract HTML"""
    url = "https://en.wikipedia.org/wiki/Betta"
    webdatasource = DataSource(WebSourceType())
    html = webdatasource.extract_data(url)

    assert "<!doctype html>" in html.lower(), "html content not extracted from url"