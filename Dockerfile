FROM python:3.8

WORKDIR /code

COPY . .

RUN pip install -e .

ENTRYPOINT ["paji"]
