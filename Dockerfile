FROM python:3.6
LABEL maintainer="lorenz.vanthillo@gmail.com"
COPY . /app
WORKDIR /app
pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
