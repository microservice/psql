FROM          python:3.7-alpine

RUN           mkdir /app

COPY          requirements.txt /app
RUN           pip install -r /app/requirements.txt

COPY          app.py /app

ENTRYPOINT    ["python", "/app/app.py"]
