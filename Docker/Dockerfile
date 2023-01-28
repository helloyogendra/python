#Specifying the base image name - FROM command is mandatory

FROM python:alpine

RUN apk update
RUN apk add git
RUN apk add curl

RUN touch abc.py
RUN echo "print('test command')" > abc.py 

CMD ["python", "abc.py"]