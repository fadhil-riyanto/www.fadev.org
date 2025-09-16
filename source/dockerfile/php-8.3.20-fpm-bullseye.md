# php:8.3.20-fpm-bullseye + nginx

```dockerfile
FROM php:8.3.20-fpm-bullseye 

RUN apt-get update && apt-get install -y libpq-dev
RUN docker-php-ext-install pdo pdo_pgsql

COPY . /app
WORKDIR /app

COPY ./docker/fpm/www.conf /usr/local/etc/php-fpm.d/www.conf
# karna php-fpm running pakai user www-data
RUN chown -R www-data:www-data /app/storage


CMD [ "php-fpm" ]
```

default.conf (nginx)
```dockerfile
server {
    listen       80;
    server_name  localhost;

    access_log  off;
    root /app/public;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }


    location ~ \.php$ {

        fastcgi_pass   php:9000; 
        fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param  DOCUMENT_ROOT $document_root;
        include        fastcgi_params;
    }
}

```

www.conf

```

[www]
access.log = /dev/null

user = www-data
group = www-data

listen = 0.0.0.0:9000

pm = dynamic
pm.max_children = 5
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3
```