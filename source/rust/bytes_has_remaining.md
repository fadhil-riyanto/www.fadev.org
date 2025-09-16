# Rust bytes has_remaining() method

this function return whatever any best left on buffer. example, let make simple tcp/ip

```rust
impl Connection {
    pub fn new(stream: TcpStream) -> Connection {
        Connection {
            stream: BufWriter::new(stream),
            buffer: BytesMut::with_capacity(4096)
        }

    }

    pub async fn read(&mut self) 
        -> std::result::Result<Option<Frame>, Box<dyn std::error::Error + Send + Sync>> {
        
        let _ = self.stream.read_buf(&mut self.buffer).await;
        println!("hasremaining: {}", self.buffer.has_remaining());
        
        while self.buffer.has_remaining() {
            let bytes = self.buffer.get_u8();
            println!("{} -> {}", bytes as char, self.buffer.has_remaining());
        }

        println!("{}", self.buffer.has_remaining());
        // Frame::check(&mut self.buffer);

        Ok(Some(Frame::Null))
    }
}
```

let's see the server result using `ncat`

![ncat-result](../_images/tcp-ncat-snapshot.png)

which the input is something look like this
```sh
[22:55:41] fadhil_riyanto@integral2 /home/fadhil_riyanto [SIGINT]
> ncat 127.0.0.1 6380
abc

```

from this output, we know
```
hasremaining: true <--- this is initial, didn't mean anything
a -> true <--- a already read, but next char is b, why this is true
b -> true <--- next is c, also true
c -> true <--- next is \n char, also true

 -> false <--- this is false because no next chars
false <--- confirm
```

Also, `get_u8` returns the first byte in the buffer. Each time it's called, it advances the position, so subsequent calls return the next bytes.