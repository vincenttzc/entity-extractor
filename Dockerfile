FROM python:3.8-buster
COPY . .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN python src/download_nltk.py
ENV PORT 8080
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 src.app:app
