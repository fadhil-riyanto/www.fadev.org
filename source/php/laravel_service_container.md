# laravel service container

date: Sun Jun  8 11:47:02 PM WIB 2025

links

- [https://laravel.com/docs/12.x/container#introduction](https://laravel.com/docs/12.x/container#introduction)

## making
untuk membuat service container, katakanlah isi class ctx yang namanya Google\Client. dia mereturn $client. maka kita harus bikin

```sh
php artisan make:provider GoogleApis
```

nama GoogleApis bebas. lalu cek di folder `./app/Providers/GoogleApis.php` harusnya ada, dan di file `./bootstrap/providers.php` akan ada 

```php
<?php

return [
    App\Providers\AppServiceProvider::class,
    App\Providers\GoogleApis::class,
];

```

ada `App\Providers\GoogleApis::class` maksudnya.

## registering

dari service provider yang baru saja dibuat, akan ada 2 method, yaitu

- `public function register(): void`: boot ini entry dari service, nilai ctx ctx dsb biasanya diload disini
- `public function boot(): void`: func ini dipanggil kalau semua service sudah jalan, misal service route di register, tapi method untuk nambahin route routenya. ada di boot

general structure nya (file `./app/Providers/AppServiceProvider.php`)

```php
<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        //
    }
}

```

## the inside of register function

docs tentang 
- binding -> [https://laravel.com/docs/12.x/container#simple-bindings](https://laravel.com/docs/12.x/container#simple-bindings)
- singleton -> [https://laravel.com/docs/12.x/container#binding-a-singleton](https://laravel.com/docs/12.x/container#binding-a-singleton)

perbedaanya, `bind` auto buat fresh ctx tiap kali request datang, sedangkan `singleton` hanya buat sekali, contoh konkret `singleton` adalah ctx koneksi mongodb, kita cukup pakai sekali saja, untuk semua container

ini contoh googleclient

```php
// this code is inside of register() func
$this->app->singleton(Client::class, function (Application $app) {
    $client = new Client();
    $client->setApplicationName(env("G_SSO_NAME"));
    $client->setClientId(env("G_SSO_CLIENT_ID"));
    $client->setClientSecret(env("G_SSO_CLIENT_SECRET"));
    $client->setRedirectUri(env("G_SSO_REDIRECT_URI"));
    $client->addScope([
        Service\Oauth2::USERINFO_EMAIL,
        Service\Oauth2::USERINFO_PROFILE
    ]);
    $client->setAccessType('offline');
    $client->setLoginHint('your_email@gmail.com');

    return $client;
});
```

catatan: `use Illuminate\Contracts\Foundation\Application` itu ctx bawaan laravel buat ngebind.

## how to use
lokasi: controller

kita tinggal panggil saja class (milik aslinya)

contoh

```php
use Google\Client;

class Randomclass extends Controller

{
    /**

     * Create a new controller instance.

     */

    public function __construct(

        protected Client $client,

    ) {}

    public function use_it() {
    	$this->client->some_google_method();
        // $this->client was initialized
    }
}
```