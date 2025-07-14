FROM python:3.10-slim
RUN mkdir /app
COPY ./requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./src/app.py ./app/src
WORKDIR /app/src/

CMD ["python", "app.py"]