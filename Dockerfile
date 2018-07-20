#FROM ubuntu:latest
#MAINTAINER Stanojevic Stefan "stanojevic.stefan23@gmail.com"
##RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential#
#COPY ./requirements.txt /app/requirements.txt
#WORKDIR /app
#RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["app.py"]

FROM ubuntu:latest

MAINTAINER Stanojevic Stefan "stanojevic.stefan23@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]