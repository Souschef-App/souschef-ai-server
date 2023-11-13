FROM python:3.11-slim-bookworm

COPY pyproject.toml .
COPY poetry.lock .

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

WORKDIR /workspace

COPY app/ app/

COPY main.py main.py

CMD ["python",  "main.py"]

