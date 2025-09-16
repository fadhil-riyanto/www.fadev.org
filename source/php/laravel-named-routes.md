# laravel named routes

ref: [https://laravel.com/docs/12.x/routing#named-routes](https://laravel.com/docs/12.x/routing#named-routes)

examples

```php
Route::prefix('auth')->group(function () {
    Route::prefix('google')->group(function () {
        Route::get('/redirect', [Controllers\GoogleAuthController::class, 'redirect'])
            ->name("auth.google.redirect");
        Route::get('/callback', [Controllers\GoogleAuthController::class, 'callback'])
            ->name("auth.google.callback");;
    });

    /* .. */
});
```

acces it (in blade)

```php
<h1>{{ route("auth.google.callback"); }}</h1>
```