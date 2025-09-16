# php-8.3 debian v11 (bullseye) dev-env

CREATED: `Fri Jun  6 06:32:35 PM WIB 2025`

```docker
FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive
# initial, refresh repo first
RUN apt-get update

# this install base package that need in order to download gpg key (curl, and gnupg)
RUN apt-get install -y ca-certificates
RUN apt-get install -y apt-transport-https
RUN apt-get install -y lsb-release
RUN apt-get install -y gnupg
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y unzip

# add ondrej\PPA
RUN curl -fsSL https://packages.sury.org/php/apt.gpg | gpg --dearmor -o /etc/apt/trusted.gpg.d/php.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php.list

# install actual package, php-xml & php-mbstring is needed by composer. 
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y php8.3
RUN apt-get install -y php8.3-curl
RUN apt-get install -y php8.3-xml
RUN apt-get install -y php8.3-mbstring

# download composer
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php \
        && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
        && rm composer-setup.php

COPY . /app
WORKDIR /app

EXPOSE 4444

# install composer
RUN composer install
CMD [ "php", "-S", "0.0.0.0:4444", "-t", "public" ]
```