FROM python:3

FROM ubuntu:latest

workdir /app

COPY . /app/
 
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y wget

RUN pip install --upgrade pip 

RUN pip install deepspeech
RUN pip install numpy 
RUN pip install flask

RUN wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm

CMD ["python3", "flask_app.py"]


