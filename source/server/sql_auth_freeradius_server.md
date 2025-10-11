# SQL authentication freeradius server

first, desclaimer. I use Ubuntu 24.04.2 LTS that running on Archlinux qemu host. so this is not host machine.
big thanks for linux netdev that makes local networking possible.

first, lets configure postgresql server 

```sh
root@integral2:/home/fadhil_riyanto# su postgres
postgres@integral2:/home/fadhil_riyanto$ psql
psql (16.9 (Ubuntu 16.9-0ubuntu0.24.04.1))
Type "help" for help.

postgres=# 
```
## database setup

get it inside. then run

![image](../_images/0b31f1fb1d97b32e112694dfd750fcc3b92093645f508ce8fa438a0db2cb899fd2f0998547e4bdc11ac18ebb15bb735e6418d9fae86960146d3acfed.png)

![image](../_images/5fb4e7aa16213974a3e2db1bf3f1efbf60963f9489610aa012244e484c45351272758aedd68c41b79f1a4dac034c30e5fea04f1ab2caf5efe849df87.png)

![image](../_images/7fffd04029a9a3640c8ffc737d03ef9339da23e60c7189f3a567e733c49cc24d569843fd1e7611015a05c06dd794129b7536bf92ef2e83caaddf40aa.png)

![image](../_images/5aab65a8641c5e71d111bbb878e53009adbe5b74d8715d5adb371fd4ba81a2b0873fbed49ae237c6c816e7d779535a5c5ada5173c566ae341c83177d.png)

do not forget to allow CRUD option on all tables by running

```sql
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO radius;
```

## radius server configuration 

the sequence of config file

- `/etc/freeradius/3.0/clients.conf` <-- specify 'who' can connect, we need define it in this file
- `/etc/freeradius/3.0/users` <-- [manual authentication, using file]
- `/etc/freeradius/3.0/radiusd.conf:986` <-- this file enable sql module.
- `/etc/freeradius/3.0/mods-available/sql` <-- this file is where we configure user/pass for sql module
- `/etc/freeradius/3.0/sites-available/default` <-- sequence layer of login, 
	- first, we filter-out all args
	- then go to preprocess
	- send to log
	- chap & mschap
	- check whatever has digest
	- check whatever user@domain format
	- eap
	- files
	- lookup to sql <-- uncomment this

as root

- `/etc/freeradius/3.0/mods-enabled`
- `ln -s ../mods-available/sql ./sql`
- uncomment this line in radiusd.conf
![image](../_images/d0665ba7eb645242c298dedbe2902e18796c7216dc8896139a721fab2415fa7611195ab9422d6948f86a427b9707e760fc0221f88fc230a67758b76d.png)
- change this line to postgresql (mods-enabled/sql)
![image](../_images/fdfd7b497384b6a5c5987b572b67fa8568798a334fadc2019039dcf90b8b6d534905f22318cf4c7af41a02ab7e2343f119de684f3044167e957c3196.png)

also 
![image](../_images/8d2a7f06a33c1eb1cd47bb7d3668d313b43431c18415335eecfbd41e24ea23ebaaf5ca351afa0987d3fa16a05fa05bb81f1324b17d8e7ef5abc916b4.png)
- fill the pgsql server credentials (/etc/freeradius/3.0/mods-config/sql/main/postgresql/queries.conf) (aka raddb/sql/database/dialup.conf in rhel)

![image](../_images/88a6744259611366420a5d727c6d0340d810087dab0abf04c70d2e2470cb06d85a74c82608b32feda254e2b333978fdcb4120294454460480cb4e270.png)

### when connection failed
![image](../_images/9717e76d53ae41ea098987ea8dfb4bbe936527330f4c1b9fb7aed97549ddb79ef0ef21a1663f8d9297537cc60cb768258b9a9fd4c959a1e48539bab6.png)

### when connection succeed
![image](../_images/4591156b3d62c9d877f6ae8def706c382955e5c8440c902c5098eac584894d6d24b8218338280b7b701156eec3cb480dacdbaac0b8947828932c72b0.png)

# populating
best read: [https://wiki.freeradius.org/guide/SQL-HOWTO#populating-sql](https://wiki.freeradius.org/guide/SQL-HOWTO#populating-sql)

big thanks for freeradius developer, the sql file is located at `/etc/freeradius/3.0/mods-config/sql/main/postgresql/schema.sql`

import it with: 

```sql
psql -U radius -d radius -f /etc/freeradius/3.0/mods-config/sql/main/postgresql/schema.sql
```

# configuration
lets look at `sites-available/default`

![image](../_images/b609f49cbcdf2c21d6291c8b173e74b9b8ff663c18c5bd1314fd3ec7eae39ec65ef238a89d9522f8ded12b3bd6ff1a0bcb2b6ce5fc5bc70146bb82f3.png)

this configuration only allow authorize users that come from NAS-Port-Type == "Wireless-802.11", this is the difference

footage 1: from winbox request
![image](../_images/599e5f76e91856db04f9d4cbdadd0d4c4384d7e073c91fa187c4754eefc83424ec9ecb304d5f166ae2204b4b6c471aa531e2b41045cb487d17e7440d.png)

this one come from captive portal
![image](../_images/b3d083c9d4dd4f95275e637bbf7a9a401086cd7bce221b536e1c500bf734d96647b0171dbca68e2d0e69fa23855bde1d9c4336f32c95289db615dcc3.png)