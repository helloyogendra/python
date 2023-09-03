FROM python:alpine

WORKDIR /app

ADD *.py /app/

RUN apk update

RUN apk add vim

RUN pip install --trusted-host pypi-python.org Flask

RUN pip install --trusted-host pypi-python.org mysql-connector-python

ENV NAME Luxoft

CMD ["python", "main.py"]
















# ADD . /app
# above will add everything, including dockerfile, we don;t want that