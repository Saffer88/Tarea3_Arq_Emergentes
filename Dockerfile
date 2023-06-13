FROM python:alpine3.18

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask  

RUN apk add --no-cache sqlite

EXPOSE 5000

CMD ["python", "/app/src/app.py"]