# salt

what is salt?
salt is sodium chloride (damn)

# in cryptography

salt is a "extra entropy" that breaks precalculated hash. 
the simple way to do is concat password with salt and hash them, let's see this scenario

```php
php > echo hash("sha256", "a-password");
e9fad6b0fee5a53813e888b6a3c63a843395ab112b51495a30c1b00a0e5f89e0
```

withou salt, if `attacker` has precomputed hash, it might found that `e9fad6b0fee5a53813e888b6a3c63a843395ab112b51495a30c1b00a0e5f89e0` is correlated with `a-password`, let's add salt

```php
php > $a = new Random\Engine\Secure();
php > $salt = $a->generate();
php > echo bin2hex($salt) . "::" . hash("sha256", $salt . "a-password");
39fa561b306cc437::46ac00f5ca786405fd91205d377a83e4e35ed954b7bd6a9078d24215b8135d78
```

and, the `39fa561b306cc437::46ac00f5ca786405fd91205d377a83e4e35ed954b7bd6a9078d24215b8135d78` you can store in your db table.

we generate a CSPRNG (Cryptographically Secure Pseudorandom Number Generator), Then concat them as a salt. this is not protect a password from attacking, but make a attacker harder because its need to be re-compute the value (which is heavy, e.g bruteforcing)