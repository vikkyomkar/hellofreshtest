FROM python:2.7-alpine
MAINTAINER Vikky Omkar "vikkyomkar@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
