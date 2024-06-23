
FROM python:3.10

WORKDIR /app

COPY . /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y libgl1-mesa-glx

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD python ./app.py
