# how to use SQLX cli tools for db migration such laravel migrations

let's meet with this crate, [https://crates.io/crates/sqlx-cli](https://crates.io/crates/sqlx-cli), this tools allow you to use db migration such as laravel migration tools;

first, let's create env variable
```
export DATABASE_URL=postgres://fadhil_riyanto:<your_pass>@localhost/<target_db>
```
then, the things that we do next is only
```
sqlx migrate add -r <name>
```
running
```
sqlx migrate run
```