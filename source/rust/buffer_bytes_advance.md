# Rust buffer advance

this simple article show how buffer advance works

```rust
use bytes::Buf;

fn main() {
    let mut buf = &b"hello world"[..];

    println!("{}", String::from_utf8_lossy(buf.chunk()));

    buf.advance(6);
    println!("{}", String::from_utf8_lossy(buf.chunk()));
}

```

and the result
```rust
hello world
world
```