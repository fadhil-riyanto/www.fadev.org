# Rust tonic gRPC server build process

topik ini khusus membahas gRPC di rust,

## build
contoh template build rs:
```rust
use std::{env, path::PathBuf};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // let out_dir = PathBuf::from(env::var("OUT_DIR").unwrap());
    let out_dir = PathBuf::from(
        "/home/fadhil_riyanto/BALI64/fadev-service-rs/rpc/src/pb".to_string()
    );

    println!("cargo:warning=start build!");
    
    tonic_build::configure()
        .build_server(true)
        .build_client(false)
        .file_descriptor_set_path(out_dir.join("random_service.bin"))
        .compile_protos(
            &["proto/random_service.proto"], 
            &["proto"]
        )?;


    Ok(())
}

```

nb:
 - `file_descriptor_set_path`: dipakai sebagai reflection, bakal ketemu kalau pakai grpcurl.
 - `build_server` dan `build_client`: disini ada 2 mode build, untuk server atau untuk client. maka kita set server true, client false
 - `compile_protos`: masing2 berisi 2 param yg menerima slice, param pertama berisi lokasi protobuf, param kedua berisi root foldernya.

 anda bisa lihat-lihat contoh lain disini: [https://github.com/hyperium/tonic/tree/master/examples](https://github.com/hyperium/tonic/tree/master/examples)

optional:
 - use `.out_dir()` ketimbang harus nurut dengan apa yang OUT_DIR katakan

## OUT_DIR
what it is, simplenya `OUT_DIR` ini akan diset jika protobuf sudah di compile, dalam artian, file `*.proto` diubah jadi kumpulan file `*.rs` yang bakal di include sama macro, kemudian di compile

urutan compile adalah, macro dievaluasi dulu, baru compile, sampai sini masuk akal. ini macro signature nya

```rust
#[macro_export]
macro_rules! include_proto {
    ($package: tt) => {
        include!(concat!(env!("OUT_DIR"), concat!("/", $package, ".rs")));
    };
}
```

tambahan info bisa baca2 sendiri disini: [https://doc.rust-lang.org/cargo/reference/environment-variables.html#environment-variables-cargo-sets-for-build-scripts](https://doc.rust-lang.org/cargo/reference/environment-variables.html#environment-variables-cargo-sets-for-build-scripts), dan jg biasanya ini akan diinclude ke sebuah file handler. kira kira seperti itu

