import spacy
import nltk
import pickle


nltk.download("punkt")


class Model:
    def __init__(self):
        # python -m spacy download en_core_web_sm
        self.model = spacy.load(
            "en_core_web_sm",
            disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"],
        )

    def predict(self, data):
        sentences = self._split_to_sentence(data)
        result = []
        for text in sentences:
            result += self._predict_single(text)

        return result

    def _predict_single(self, text):
        result_single = []
        doc = self.model(text)
        ents = doc.ents
        if len(ents) > 0:
            for ent in ents:
                result_single.append([str(ent), text])

        return result_single

    def _split_to_sentence(self, text_body):
        text_list = nltk.tokenize.sent_tokenize(text_body)
        return text_list


if __name__ == "__main__":
    model = Model()
    with open("test_text.txt", "r", encoding="utf-8") as f:
        data = f.read()
    result = model.predict(data)

    with open("test_result.txt", "wb") as file:
        pickle.dump(result, file)

    print(result[50])
