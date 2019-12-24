FROM python:3.6
ENV http_proxy http://proxy-chain.xxx.com:911/
ENV https_proxy http://proxy-chain.xxx.com:912/
LABEL maintainer="lorenz.vanthillo@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
