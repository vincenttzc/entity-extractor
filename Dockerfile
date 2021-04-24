FROM python:3.8-buster
COPY . .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN python src/download_nltk.py

EXPOSE 80
CMD uvicorn src.app:app --host 0.0.0.0 --port 80