FROM php:7.2-apache
RUN apt-get update && apt-get install -y openssl zip unzip git --no-install-recommends \
    && docker-php-ext-install pdo_mysql
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
WORKDIR /var/www/recommendation-system-app
COPY . /var/www/recommendation-system-app
RUN composer install
ENTRYPOINT ["php", "artisan", "serve", "--host=0.0.0.0", "--port=80"]
EXPOSE 80
