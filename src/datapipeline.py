import requests
from bs4 import BeautifulSoup
from bs4.element import Comment


class DataPipeline:
    def __init__(self, blacklist):
        self.blacklist = blacklist

    def __call__(self, url):
        text_body = self._get_text_from_url(url)
        return text_body

    def _get_text_from_url(self, url):
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "html.parser")
        texts = soup.findAll(text=True)
        visible_texts = filter(self._tag_visible, texts)

        return " ".join(t.strip() for t in visible_texts)

    def _tag_visible(self, element):
        if element.parent.name in self.blacklist:
            return False
        if isinstance(element, Comment):
            return False
        return True


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/GIC_(Singaporean_sovereign_wealth_fund)"
    blacklist = ["style", "script", "head", "title", "meta", "[document]", "aside"]

    pipeline = DataPipeline(blacklist)
    output = pipeline(url)

    with open("test_text.txt", "w", encoding="utf-8") as file:
        file.write(output)

    print(output)