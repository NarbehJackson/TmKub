FROM python:3.7-alpine3.9
RUN apk update
RUN apk add gcc g++ make libffi-dev openssl-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]