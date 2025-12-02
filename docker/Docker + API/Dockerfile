FROM python:3.12-slim

WORKDIR /app

RUN pip install flask

COPY app.py .

EXPOSE 5000

CMD ["python","app.py"]

#docker build -t mon-app
#docker run -p 4900:5000 mon-app
