# Rust tokio-postgres connection config example

first, this is example from the documentation

```rust
 let (client, conn_ctx) = tokio_postgres::connect("host=localhost user=postgres", NoTls);
```

then, we want to convert it into config like ctx. [see this](https://docs.rs/postgres/latest/postgres/config/struct.Config.html)

```rust
use tokio_postgres::{NoTls, Error};

#[tokio::main]
async fn main() {
        let mut config = postgres::config::Config::new();
        config.host("localhost");
        config.user("fadhil_riyanto");
        config.password("1921684338");

        let client_ret = config.connect(NoTls);


}
```

