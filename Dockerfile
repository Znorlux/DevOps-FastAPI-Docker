FROM python:3.13.0rc3-alpine3.19

WORKDIR /app

COPY ruta2/. /app/ruta2
COPY endpoint1.html /app/
COPY endpoint1_2.html /app/
COPY index_basico.html /app/
COPY index.html /app/
COPY requirements.txt /app/
COPY server.py /app/
COPY main.py /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8432

CMD [ "python", "/app/server.py" ]