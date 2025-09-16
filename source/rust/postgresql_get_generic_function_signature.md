# postgresql - get() generic function signature

In someday, i found
```rust
#[track_caller]
    pub fn get<'a, I, T>(&'a self, idx: I) -> T
    where
        I: RowIndex + fmt::Display,
        T: FromSql<'a>,
    {
        match self.get_inner(&idx) {
            Ok(ok) => ok,
            Err(err) => panic!("error retrieving column {}: {}", idx, err),
        }
    }
```

some sort of notes:
- https://doc.rust-lang.org/rust-by-example/generics.html
- https://serokell.io/blog/rust-generics

how to call it
```rust
let data2 = data_actual[0].get::<_, i32>(0);
```