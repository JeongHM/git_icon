FROM python:3.6.1-alpine
ADD . /usr/dockerapp 
WORKDIR /usr/dockerapp
RUN pip install -r requirements.txt
CMD ["python", "./app.py"]

