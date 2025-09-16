# php:8.3.20-bullseye dev env

this is also works for laravel

```php
FROM php:8.3.20-bullseye

RUN apt-get update && apt-get install -y \
        curl \ 
        libpq-dev \
        git \
        unzip
RUN docker-php-ext-install pdo pdo_pgsql

COPY . /app
WORKDIR /app

RUN curl -sS https://getcomposer.org/installer -o composer-setup.php \
        && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
        && rm composer-setup.php

RUN composer install

CMD [ "php", "-S", "0.0.0.0:10302", "-t", "public" ]
```

compose.yml

```
volumes:
  storage:
  db_data:

networks:
  veth_network:
    driver: bridge

services:
  google_sso:
    image: php:8.3.20-bullseye
    build:
      context: .
      dockerfile: dev.backend.Dockerfile
    environment:
      - docker=true
      - DB_HOST=pgsql_db
      - DB_PORT=5432
      - DB_USERNAME=postgres
      - DB_PASSWORD=<PASSWD>
      - DB_DATABASE=google_sso_dev
      - G_SSO_NAME=google-sso-login
      - G_SSO_CLIENT_ID=ABC
      - G_SSO_CLIENT_SECRET=DEF
      - G_SSO_REDIRECT_URI=http://localhost:10302/auth/callback
    ports:
      - "10302:10302"
    networks:
      - veth_network
    volumes:
      - .:/app
      - storage:/app/storage
    depends_on:
      - pgsql_db

  pgsql_db:
    image: postgres:17.5-bullseye
    restart: always
    shm_size: 128mb
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=<PASSWD>
      - POSTGRES_DB=google_sso_dev
    networks:
      - veth_network
    volumes:
      - db_data:/var/lib/postgresql/data
  
  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
    networks:
      - veth_network
    depends_on:
      - pgsql_db
```

CATATAN unik: ketika ping `pgsql_db` dari xxx container, ia otomatis resolve dns nya.