# php-fpm config

file ini biasanya ada di 
- `/usr/local/etc/php-fpm.d/www.conf` (di docker php-fpm)
- `/etc/php/8.3/fpm/pool.d/www.conf` (di debian bullseye)

intinya, tidak pasti haha.

## config structure

general structure nya seperti ini kalau ';' dihilangkan

```ini
[www]
user = www-data
group = www-data
listen = /run/php/php8.3-fpm.sock
listen.owner = www-data
listen.group = www-data
pm = dynamic
pm.max_children = 5
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3
```

## config global (WIP)
lokasi config ini ada di 

`/etc/php/php-fpm.conf`

## config untuk pool (each)

best read [https://www.php.net/manual/en/install.fpm.configuration.php](https://www.php.net/manual/en/install.fpm.configuration.php)

- <b>[pool_name]</b>
	intinya ini unique, tidak ada yang sama
- <b>user / group</b>
	- `user`: dimana child process akan di run (as user?)
	- `group`: liat /etc/passwd
- <b>listen</b>
	- `listen`: dimana daemon akan listen yg nanti akan di reverse proxy oleh nginx, 
		nilai defaultnya biasanya `/run/php/php8.3-fpm.sock` atau `127.0.0.1:9000`, contoh:
		- `ip.add.re.ss:port`
		- `[ip:6:addr:ess]:port`
		- `port`
		- /path/to/unix/socket
	
	- `listen.backlog`: jumlah queue pending connection yang bisa di hold
	- `listen.owner`: configure ke mana kah `/run/php/php8.3-fpm.sock` itu ownernya
	- `listen.group`: same as `listen.owner`
	- `listen.mode`: nomor permission si `/run/php/php8.3-fpm.sock` listen
	- `listen.acl_users`: WIP
	- `listen.acl_groups`: WIP
	- `listen.allowed_clients`: set dari mana FCGI boleh diakses, di kasus nginx, mostly 127.0.0.1, except docker, dia pakai br-xxxxxx yang ip nya pasti bukan 127.0.0.1
	- `listen.setfib`: WIP