FROM python:3.12

RUN mkdir /booking

WORKDIR /booking

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY app app
COPY fixtures fixtures
COPY scripts scripts
COPY alembic.ini .
COPY pytest.ini .

RUN mv scripts / \
    && chmod +x /scripts/*

ENTRYPOINT ["/scripts/entrypoint.sh"]