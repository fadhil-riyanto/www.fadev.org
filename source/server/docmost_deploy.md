# deploy Docmost on server

please read this doc first, [https://docmost.com/docs/installation](https://docmost.com/docs/installation)

## docker compose config


```
version: "3"

services:
  docmost:
    image: docmost/docmost:latest
    depends_on:
      - db
      - redis
    environment:
      APP_URL: "http://localhost:3000"
      APP_SECRET: "REPLACE_WITH_LONG_SECRET"
      DATABASE_URL: "postgresql://docmost:STRONG_DB_PASSWORD@db:5432/docmost?schema=public"
      REDIS_URL: "redis://redis:6379"
    ports:
      - "3000:3000"
    restart: unless-stopped
    volumes:
      - docmost:/app/data/storage

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: docmost
      POSTGRES_USER: docmost
      POSTGRES_PASSWORD: STRONG_DB_PASSWORD
    restart: unless-stopped
    volumes:
      - db_data:/var/lib/postgresql/data

  redis:
    image: redis:7.2-alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data

volumes:
  docmost:
  db_data:
  redis_data:
```

replace your `STRONG_DB_PASSWORD` with `openssl rand -hex 10`, and `REPLACE_WITH_LONG_SECRET` with `openssl rand -hex 32`, and `APP_URL`, for example, in my case is `https://docmost.fadev.org`

run `docker compose run`

## setup reverse proxy (nginx)
go to `/etc/nginx/sites-enabled`, and create a clone with `cp default docmost.fadev.org`

fill it like this

```conf
server_name docmost.fadev.org;

location / {
	# First attempt to serve request as file, then
	# as directory, then fall back to displaying a 404.
	#try_files $uri $uri/ =404;

	proxy_pass http://127.0.0.1:3000;
}

location /socket.io/ {
	proxy_pass http://127.0.0.1:3000;
	proxy_http_version 1.1;
	proxy_set_header Upgrade $http_upgrade;
	proxy_set_header Connection "upgrade";
	proxy_set_header Host $host;
}

location /collab {
	proxy_pass http://127.0.0.1:3000;
	proxy_http_version 1.1;
	proxy_set_header Upgrade $http_upgrade;
	proxy_set_header Connection "upgrade";
	proxy_set_header Host $host;
}

```

## HTTPS

run

- `sudo apt install certbot python3-certbot-nginx`
- `sudo certbot --nginx -d docmost.fadev.org`

## Firewall
allow port 443