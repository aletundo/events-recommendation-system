FROM php:7.2-apache
RUN apt-get update -y && apt-get install -y openssl zip unzip git
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN docker-php-ext-install pdo pdo_mysql mbstring
WORKDIR /app
COPY . /app
RUN composer install
RUN cp .env.example .env
RUN php artisan key:generate
CMD php artisan serve --host=0.0.0.0 --port=8080
EXPOSE 8080
