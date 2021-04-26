from src.model import Model


def test_model_predict():
    """Test if model can extract entities and accompanying sentence"""
    with open("tests/processed_html_text.txt", "r", encoding="utf-8") as f:
        data = f.read()

    model = Model()
    output = model.predict(data)

    assert len(output) > 0, "model did not return any prediction"
    assert len(output[0]) == 2, "model did not return entity and sentence"