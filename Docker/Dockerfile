#Specifying the base image name - FROM command is mandatory

FROM python:alpine

LABEL Writter="Yogendra"

WORKDIR /app

#WORKDIR /opt

COPY Code.py app/Code.py

ADD . /app

CMD ["python", "Code.py"]