FROM ubuntu

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 9096

CMD ["python","main.py"]

