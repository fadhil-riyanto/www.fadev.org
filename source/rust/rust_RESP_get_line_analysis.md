# Rust RESP get_line analysis

if we look at simple tokio redis example (mini redis), we can see how the data is parsed. look at this

the resp is generally read something like this `+abc\r\n'

this is the code that actually crop down the buffer

```rust
fn get_line<'a>(src: &mut Cursor<&'a [u8]>) -> Result<&'a [u8], Error> {
    // Scan the bytes directly
    let start = src.position() as usize;
    // Scan to the second to last byte
    let end = src.get_ref().len() - 1;

    for i in start..end {
        if src.get_ref()[i] == b'\r' && src.get_ref()[i + 1] == b'\n' {
            // We found a line, update the position to be *after* the \n
            src.set_position((i + 2) as u64);

            // Return the line
            return Ok(&src.get_ref()[start..i]);
        }
    }

    Err(Error::Incomplete)
}
```

and I will show you how they works (algorithm)

# variables setup
we have `start` and `end`, which consist of 

```rust
let start = src.position() as usize;
let end = src.get_ref().len() - 1;
```

the `src.position()` always return 0, also depending on the context. `src.get_ref().len()` return the length of the buffer, for example, `+rand\n\n` has length 7.

because we wan't to read two chars at the end, which is \r and \n

so we substract length with 1, *this is avoid buffer overflow*

suppose this situation:
buf: `+rand\n\n`

when we add everything with 1, we got this
idx: `012345 6 7`, it is idx[7]is found? no, so we need to sub with 1, the idx is something like this
idx: `012345 6`, no overflow

then we check the `i` and `i + 1`, make sure there is \r\n

# set position
now, we set the cursor to the next incoming buffer. which after \r\n

```rust
src.set_position((i + 2) as u64);
```
suppose:

```
+rand\r\n+randomsomething\r\n
012345 6 ^ 
^^   ^   this is i + 2, indicates next buffer
ii+1 orig i
```