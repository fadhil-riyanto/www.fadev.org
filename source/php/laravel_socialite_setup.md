# laravel Socialite setup

Mon Jun  9 05:49:13 AM WIB 2025

## setup
lihat `config/services.php`, disana hanya ada slack, maka kita tambahin

```php
    'google' => [
        'client_id' => env('G_SSO_CLIENT_ID'),
        'client_secret' => env('G_SSO_CLIENT_SECRET'),
        'redirect' => env('G_SSO_REDIRECT_URI'),
        'name' => env('G_SSO_NAME'),
    ],
```

## usage
dapatkan link permintaan akses, pakai 

```php
return Socialite::driver('google')->redirect();
```

ketika user sudah klik continue & accept share datanya, akan dikirimkan callback, pasang ini ke callback

```php
$user = Socialite::driver('google')->user();
dd($user);
```