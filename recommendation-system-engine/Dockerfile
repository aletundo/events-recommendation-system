FROM python:alpine
WORKDIR /var/www/recommendation-system-engine
COPY . /var/www/recommendation-system-engine
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "src/app.py"]
