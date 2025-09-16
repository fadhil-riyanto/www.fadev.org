# Rust cursor, How it works

Cursor in rust basically just a in-memory implementation of Seek. [see fseek() here](https://en.cppreference.com/w/c/io/fseek)

Imagine, we have a file. and this is representation of contents

```
abcde
```

seek start from 1, is `bcde`, start from 2 is `cde` and so-on, this is also happen when we use seek from end, for example, seek end -1 is mean `e`, -2 is `de`, etc.

# From code perspective

this is signature of cursor
```rust
pub struct Cursor<T> {
    inner: T,
    pos: u64,
}
``` 

and also, this struct implement [Write](https://doc.rust-lang.org/src/std/io/cursor.rs.html#566) and [Seek](https://doc.rust-lang.org/src/std/io/cursor.rs.html#289)

so, in order to understanding this concept, let code first in C

```c

#include <string.h>
#include <stdlib.h>
#include <stdio.h>

struct seekfd {
    FILE                *file;
};

int start_open(struct seekfd *seekfd) {
    seekfd->file = fopen("a.txt", "r");

    if (seekfd->file == NULL) {
        fprintf(stderr, "%s", "error");
        return -1;
    }
}

int do_op(struct seekfd *seekfd) {
    char allocated_buf[2048];
    memset(allocated_buf, 0, 2048);

    fseek(seekfd->file, 1, SEEK_SET);
    int ret = fread(allocated_buf, 1, 3, seekfd->file);

    printf("%s", allocated_buf);
}

int main() {
    struct seekfd seekfd;

    int ret = start_open(&seekfd);
    if (ret < 0) {
        return -9;
    }

    ret = do_op(&seekfd);
    if (ret < 0) {
        return ret;
    }
}
```

compile with
```sh
clang fseek.c -o p -g
```

next step, create dummy files named a.txt with content `abcdefghijklmnopqr`

first run with `fseek(seekfd->file, 0, SEEK_SET);` = `abc`
second run with `fseek(seekfd->file, 1, SEEK_SET);` = `bcd`
etc...

this concept is basically same in Rust

# Rust context
this is small example show Seek works (in-memory) instead utilize *real* file

```rust
use std::io::prelude::*;
use std::io::{self, SeekFrom};
use std::io::Cursor;

fn write_bytes<W: Write + Seek>(mut w: W) -> io::Result<()> {
    w.seek(SeekFrom::Start(5))?;
    
    for i in 1..6 {
        w.write(&[i])?;
    }

    Ok(())
}


fn main() {
    let mut buf = Cursor::new(vec![0; 20]);
    write_bytes(&mut buf).unwrap();
    println!("{:?}", &buf.get_ref()); // print vector
}

```

this is the output
```
[0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

instead, we change `SeekFrom::Start(5)` with `SeekFrom::Start(10)`, the write will started at offset 10. this is the output
```
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
```