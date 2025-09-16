# laravel pgsql migration setup

Mon Jun  9 05:56:55 AM WIB 2025

PGSQL datatype to laravel mapping function: [https://api.laravel.com/docs/12.x/Illuminate/Database/Schema/Blueprint.html](https://api.laravel.com/docs/12.x/Illuminate/Database/Schema/Blueprint.html)

buat migrationnya dengan
```sh
php artisan make:migration create_table_abc
```

run
```sh
php artisan migrate
```

rollback terbaru
```sh
php artisan migrate --rollback 1
```
