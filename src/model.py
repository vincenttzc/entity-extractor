from typing import List

import spacy
import nltk


nltk.download("punkt")


class Model:
    """Class to create model object that predicts entities from text"""

    def __init__(self):
        """Constructor method"""
        self.model = spacy.load(
            "en_core_web_sm",
            disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"],
        )

    def predict(self, data: str) -> List[List[str]]:
        """Takes in string of text and predicts entities in it. Sublist contains
        entity and the sentence containing the entity

        Args:
            data (str): text body

        Returns:
            List[List[str]]: model output of entity and sentence with entity
        """
        sentences = self._split_to_sentence(data)
        result = []
        for text in sentences:
            result += self._predict_single(text)

        return result

    def _predict_single(self, text: str) -> List[List[str]]:
        """Private methos to predicts entities for single sentence

        Args:
            text (str): single sentence

        Returns:
            List[List[str]]: List of List containing entity and sentence.
            Sentence will be repeated if it contains multiple entities
        """
        result_single = []
        doc = self.model(text)
        ents = doc.ents
        if len(ents) > 0:
            for ent in ents:
                result_single.append([str(ent), text])

        return result_single

    def _split_to_sentence(self, text_body: str) -> List[str]:
        """Private method to split text body to sentences

        Args:
            text_body (str): text body

        Returns:
            List[str]: list of sentences
        """
        text_list = nltk.tokenize.sent_tokenize(text_body)
        return text_list
