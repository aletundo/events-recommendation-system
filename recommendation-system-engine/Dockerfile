FROM strayge/alpine-py3-numpy-scipy:latest
WORKDIR /var/www/recommendation-system-engine
COPY ./requirements.txt /var/www/recommendation-system-engine/requirements.txt
RUN pip install -r requirements.txt
COPY . /var/www/recommendation-system-engine
EXPOSE 5000
ENTRYPOINT ["python", "src/app.py"]
