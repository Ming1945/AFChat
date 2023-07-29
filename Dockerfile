FROM python:3.8-slim-buster

WORKDIR /afchat

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"] 