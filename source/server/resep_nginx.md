# resep nginx oleh pak hanif

cuplikan config nginx di server, cc [@hansputera](https://github.com/hansputera)

```

server {
        listen 80; # tanpa server_default
        listen [::]:80;

        root /var/www/html/blablabla.fadev.org;
        
        index index.php index.html index.htm index.nginx-debian.html;

        server_name blablabla.fadev.org;

        location ~ \.php$ {
                include snippets/fastcgi-php.conf;

                fastcgi_pass unix:/run/php/php-fpm.sock;
        }
}

```