# installing tymon/jwt-auth with custom guard

now, we will install this package as is with custom guard. so we do not use `web` guard.

# installing

read [https://jwt-auth.readthedocs.io/en/develop/laravel-installation/](https://jwt-auth.readthedocs.io/en/develop/laravel-installation/) please

do the step until reached `php artisan jwt:secret`, skip lumen Installation please

# quickstart 
please read [php/custom_auth_guard_w_tables.md](/php/custom_auth_guard_w_tables.md) first, then replace this

```php
'guest' => [
    'driver' => 'jwt',
    'provider' => 'guest_users',
],
```

in your `./config/auth.php` file, just like this

![image](../_images/054150e05a7b1c8c584febefb9460cd7ae34110ff589e5c8cac4c20e89f137da080cb3fe84711c582f0f04f39d99e3a0caaf7d5c95f96858e2afdc0f.png)

then, make sure your custom guard class is implement `Tymon\JWTAuth\Contracts\JWTSubject`, you can see the location of models class

example, in `./config/auth.php`

![image](../_images/ae5832b0d60ad775cb9f2abfd1f69d844be87529528c2a9c1895f11c10ec88d26d15e2c2ad8e6295c020333d0f9f8a2fc800018d94171df3564f0097.png)

just make it like this

![image](../_images/ae3db2de9d514e1eb4c3ca63b13344280f8133638bb908d07ab1622b6073fcc57336f374fcfadf7d0da5e3bfe65f38fb255e16abece6ad2bd2c05c4c.png)

# middleware & routing config

this section you only need to do 

```php
Route::get('/callback', [Controllers\Guest\GoogleAuthController::class, 'callback'])
            ->name("auth.google.callback")
            ->middleware("guest");
```

change with your own routing

# PoC
FIRST, we use `callback` method, so the inside of `callback` method body should look like this

```php
packed_arr = [
    "email" => $email,
    "password" => "password"
];

$token = Auth::guard("guest")->attempt($packed_arr);

if ($token) {
    return  $this->respondWithToken($token);
} else {
    return response()->json(['error' => 'Invalid credentials'], 401);
}
```

`respondWithToken` method

```php
protected function respondWithToken($token)
    {
        return response()->json([
            'access_token' => $token,
            'token_type' => 'bearer',
            'expires_in' => Auth::guard("guest")->factory()->getTTL() * 60
        ]);
    }
```