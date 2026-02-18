FROM python:3.12-slim

RUN pip install --no-cache-dir "reporails-cli>=0.4.0"

WORKDIR /rules

ENTRYPOINT ["ails", "test", "--rules-root", "/rules"]
