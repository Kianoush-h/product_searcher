FROM python:3.6.9

WORKDIR /user/src/app


COPY . .

RUN apt-get update
RUN apt-get upgrade -y

RUN apt install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install -r req.txt
RUN pip3 install colour
RUN pip3 install sqlalchemy

ENTRYPOINT ["python3", "app.py"]