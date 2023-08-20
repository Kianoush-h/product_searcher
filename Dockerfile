FROM python:3.6.9

WORKDIR /user/src/app


COPY . .

RUN apt-get update
RUN apt-get upgrade -y

RUN apt install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install -r req.txt

ENV FLASK_DEBUG=1
EXPOSE 5000

CMD ["flask","run","--host=0.0.0.0"]