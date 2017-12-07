FROM php:7.2-apache
RUN apt-get update && apt-get install -y openssl zip unzip --no-install-recommends \
    && docker-php-ext-install pdo_mysql
WORKDIR /var/www/recommendation-system-app
COPY . /var/www/recommendation-system-app
CMD php artisan serve --host=0.0.0.0 --port=80
EXPOSE 80
