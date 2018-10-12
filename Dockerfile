FROM          python:3.6.6

RUN           mkdir /app

COPY          requirements.txt /app
RUN           pip install -r /app/requirements.txt

COPY          app.py /app

ENTRYPOINT    ["python", "/app/app.py"]
