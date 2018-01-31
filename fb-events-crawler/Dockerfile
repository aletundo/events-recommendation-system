FROM python:3.6-alpine
WORKDIR /srv/fb-events-crawler
RUN apk update && apk add git
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk
COPY . .
ENTRYPOINT ["python", "src/events_crawler_by_place.py"]
