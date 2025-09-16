# Rust build logging

rust build usually don't show any output if you try to println!() in build.rs, in order to force this, use

```rust
println!("cargo:warning=start build!");
```
result
```
warning: ourcrate-rs@0.1.0: Something went wrong!
```

all docs: [https://doc.rust-lang.org/cargo/reference/build-scripts.html](https://doc.rust-lang.org/cargo/reference/build-scripts.html)