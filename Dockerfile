FROM python:3

COPY requirements.txt
COPY api.py
COPY coref.py

RUN pip install -r requirements.txt
RUN python -m spacy download en

ENTRYPOINT ["uvicorn", "api:app"]