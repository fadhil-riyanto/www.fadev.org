# laravel 12 custom auth guard + tables

Mon Jun  9 05:36:39 AM WIB 2025

di sini saya coba untuk membuat Auth::attempt [https://laravel.com/docs/12.x/authentication#authenticating-users](https://laravel.com/docs/12.x/authentication#authenticating-users), tapi bedanya, ia pakai totally different table. jadi tidak pakai table `users`

## setup model
untuk setup nya, kita buat model dulu seperti biasa pakai `php artisan make:model Xyz`, disini saya buatnya `php artisan make:model GuestUser`. lalu cek bagian `./app/Models/GuestUser.php`

normalnya class akan extends ke `Illuminate\Database\Eloquent\Model`, nah ini kita extends kan ke `Illuminate\Foundation\Auth\User`, dimana class itu kalau dirunut lagi, pasti juga nge-extends ke class Model

bukti
```php
class User extends Model implements
    AuthenticatableContract,
    AuthorizableContract,
    CanResetPasswordContract
{
    use Authenticatable, Authorizable, CanResetPassword, MustVerifyEmail;
}

```

ok, sudah. saatnya kita pindah ke model yang baru saja dibuat, isi $fillable seperti column database, jangan lupa ganti extends nya dengan `extends Authenticatable`

hasil akhir seperti ini kira2

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Foundation\Auth\User as Authenticatable;

class GuestUser extends Authenticatable
{
    protected $table = "guest_user";

    protected $fillable = [
        'name',
        'picture',
        'email',
        'password',
        'token',
        'g_auth_expires_in'
    ];
}

```

## registering guard
agar model kita bisa dibaca oleh `Auth` facade, maka kita harus registerkan dia dahulu di `./config/auth.php`, isi dahulu bagian `providers`. contoh

```php
/*
    |--------------------------------------------------------------------------
    | User Providers
    |--------------------------------------------------------------------------
    |
    | All authentication guards have a user provider, which defines how the
    | users are actually retrieved out of your database or other storage
    | system used by the application. Typically, Eloquent is utilized.
    |
    | If you have multiple user tables or models you may configure multiple
    | providers to represent the model / table. These providers may then
    | be assigned to any extra authentication guards you have defined.
    |
    | Supported: "database", "eloquent"
    |
    */

    'providers' => [
        'users' => [
            'driver' => 'eloquent',
            'model' => env('AUTH_MODEL', App\Models\User::class),
        ],
        'guest_users' => [
            'driver' => 'eloquent',
            'model' => env('AUTH_MODEL', App\Models\GuestUser::class),
        ],

        // 'users' => [
        //     'driver' => 'database',
        //     'table' => 'users',
        // ],
    ],
```

make sense kan? `guest_users` provider, ia memiliki model App\Models\GuestUser::class (note, `::class` akan return str),

setelah itu, lihat bagian atasnya, ada guards, disini kita akan naming guardsnya dan juga memberi info provider model mana yang akan dikasih, contoh

```php
/*
    |--------------------------------------------------------------------------
    | Authentication Guards
    |--------------------------------------------------------------------------
    |
    | Next, you may define every authentication guard for your application.
    | Of course, a great default configuration has been defined for you
    | which utilizes session storage plus the Eloquent user provider.
    |
    | All authentication guards have a user provider, which defines how the
    | users are actually retrieved out of your database or other storage
    | system used by the application. Typically, Eloquent is utilized.
    |
    | Supported: "session"
    |
    */

    'guards' => [
        'web' => [
            'driver' => 'session',
            'provider' => 'users',
        ],
        'guest' => [
            'driver' => 'session',
            'provider' => 'guest_users',
        ],
        
    ],
```

JFYI: `Auth::attempt()` secara default pakai guards `web`, nah kita sekarang juga bisa pakai custom, seperti ini `Auth::guard("guest")->attempt()` secara explicit kita tell laravel untuk pakai guard `guest`

## session

general login flow

```php
if (Auth::guard("guest")->attempt($packed_arr)) {

    $retq = GuestUser::where("email", $packed_arr["email"])->first();
    $retq = Auth::guard("guest")->login($retq);

    return redirect('/dashboard/index');
} else {
    dd("login failed");
}
```

`Auth::guard("guest")->attempt()` return boolean, true jika auth benar. `Auth::guard("guest")->login($retq);`  ubah state internalnya bahwa dia sudah login, lalu redirect (penting, jika tidak diredirect, nanti session akan stuck)